import asyncio
import json
import os
import logging
from simple_salesforce import Salesforce
import mcp.types as types
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class SalesforceClient:
    """Handles Salesforce operations and caching."""
    
    def __init__(self):
        self.sf = None
        self.sobjects_cache = {}

    def connect(self):
        """Establishes a connection to Salesforce using extension variables."""
        try:
            username = os.environ.get("SALESFORCE_USERNAME")
            password = os.environ.get("SALESFORCE_PASSWORD")
            security_token = os.environ.get("SALESFORCE_SECURITY_TOKEN")
            instance_url = os.environ.get("SALESFORCE_INSTANCE_URL", "https://test.salesforce.com")
            
            logging.info(f"Attempting to connect with username: {username}")
            logging.info(f"Password present: {'Yes' if password else 'No'}")
            logging.info(f"Security token present: {'Yes' if security_token else 'No'}")
            logging.info(f"Instance URL: {instance_url}")
            
            # Use the instance_url to determine domain
            domain = 'test' if 'test' in instance_url else None
            
            self.sf = Salesforce(
                username=username,
                password=password,
                security_token=security_token,
                domain=domain,
                instance_url=instance_url
            )
            logging.info("✅ Successfully connected to Salesforce")
            return True
        except Exception as e:
            logging.error(f"❌ Salesforce connection failed: {str(e)}")
            logging.error(f"❌ Username: {username}")
            return False

    def get_object_fields(self, object_name):
        """Retrieves field names, labels, and types for a specific Salesforce object."""
        if not self.sf:
            raise ValueError("❌ Salesforce connection not established.")
        if object_name not in self.sobjects_cache:
            try:
                fields = self.sf.restful(f"sobjects/{object_name}/describe")["fields"]
                self.sobjects_cache[object_name] = [
                    {
                        "label": field["label"],
                        "name": field["name"],
                        "updateable": field["updateable"],
                        "type": field["type"],
                        "length": field.get("length", None),
                        "picklistValues": field.get("picklistValues", []),
                    }
                    for field in fields
                ]
            except Exception as e:
                logging.error(f"❌ Error retrieving metadata for {object_name}: {e}")
                return json.dumps({"error": str(e)}, indent=2)
        return json.dumps(self.sobjects_cache[object_name], indent=2)

# Initialize MCP Server
server = Server("salesforce-mcp")

# Configure Salesforce Client
sf_client = SalesforceClient()
if not sf_client.connect():
    logging.error("❌ Exiting due to failed Salesforce connection.")
    exit(1)

# Register Available Tools
@server.list_tools()
async def handle_list_tools():
    return [
        types.Tool(
            name="run_soql_query",
            description="Executes a SOQL query against Salesforce",
            inputSchema={"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]},
        ),
        types.Tool(
            name="get_object_fields",
            description="Retrieves field metadata for a Salesforce object",
            inputSchema={"type": "object", "properties": {"object_name": {"type": "string"}}, "required": ["object_name"]},
        ),
    ]

@server.call_tool()
async def handle_call_tool(name, arguments):
    if name == "run_soql_query":
        query = arguments.get("query")
        if not query:
            raise ValueError("❌ Missing 'query' argument")
        try:
            results = sf_client.sf.query_all(query)
            return [types.TextContent(type="text", text=json.dumps(results, indent=2))]
        except Exception as e:
            return [types.TextContent(type="text", text=f"❌ SOQL Query failed: {e}")]

    elif name == "get_object_fields":
        object_name = arguments.get("object_name")
        if not object_name:
            raise ValueError("❌ Missing 'object_name' argument")
        results = sf_client.get_object_fields(object_name)
        return [types.TextContent(type="text", text=results)]

    else:
        raise ValueError(f"❌ Unknown tool: {name}")

async def run_mcp_server():
    logging.info("🚀 Starting MCP Server using Standard IO...")

    async with mcp.server.stdio.stdio_server() as (read, write):
        logging.info("✅ MCP Server is now running and ready for requests.")
        await server.run(
            read,
            write,
            InitializationOptions(
                server_name="salesforce-mcp",
                server_version="0.1.0",
                capabilities=server.get_capabilities(notification_options=NotificationOptions(), experimental_capabilities={}),
            ),
        )

if __name__ == "__main__":
    asyncio.run(run_mcp_server())