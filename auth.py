import os
from simple_salesforce import Salesforce

def get_salesforce_client():
    """Establishes a connection to Salesforce using extension variables"""
    try:
        username = os.environ.get("SALESFORCE_USERNAME")
        password = os.environ.get("SALESFORCE_PASSWORD")
        security_token = os.environ.get("SALESFORCE_SECURITY_TOKEN")
        instance_url = os.environ.get("SALESFORCE_INSTANCE_URL", "https://test.salesforce.com")
        
        print(f"Attempting to connect with username: {username}")
        print(f"Password present: {'Yes' if password else 'No'}")
        print(f"Security token present: {'Yes' if security_token else 'No'}")
        print(f"Instance URL: {instance_url}")
        
        # Use the instance_url to determine domain
        domain = 'test' if 'test' in instance_url else None
        
        sf = Salesforce(
            username=username,
            password=password,
            security_token=security_token,
            instance_url=instance_url,
            domain=domain
        )
        return sf
    except Exception as e:
        print(f"Detailed error connecting to Salesforce: {str(e)}")
        return None
