import os
from dotenv import load_dotenv
from simple_salesforce import Salesforce

load_dotenv()  # Load environment variables from .env file

def get_salesforce_client():
    """Establishes a connection to Salesforce"""
    try:
        username = os.getenv("SALESFORCE_USERNAME")
        password = os.getenv("SALESFORCE_PASSWORD")
        security_token = os.getenv("SALESFORCE_SECURITY_TOKEN")
        
        print(f"Attempting to connect with username: {username}")
        print(f"Password present: {'Yes' if password else 'No'}")
        print(f"Security token present: {'Yes' if security_token else 'No'}")
        
        # Append security token to password
        full_password = password + security_token
        
        sf = Salesforce(
            username=username,
            password=full_password,
            instance_url="https://test.salesforce.com",
            domain="test"
        )
        return sf
    except Exception as e:
        print(f"Detailed error connecting to Salesforce: {str(e)}")
        return None
