"""TheGooseForce CLI Entry Point"""
import asyncio
from .server import run_mcp_server

def main():
    """TheGooseForce: Salesforce integration for Goose."""
    asyncio.run(run_mcp_server())  # ✅ Properly await the coroutine

if __name__ == "__main__":
    main()
