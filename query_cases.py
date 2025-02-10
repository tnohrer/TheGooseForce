from simple_salesforce import Salesforce
import os
from dotenv import load_dotenv

def get_recent_cases():
    load_dotenv()
    
    # Connect to Salesforce
    sf = Salesforce(
        username=os.getenv('SALESFORCE_USERNAME'),
        password=os.getenv('SALESFORCE_PASSWORD'),
        security_token=os.getenv('SALESFORCE_SECURITY_TOKEN'),
        domain='test'
    )
    
    # Query cases
    query = """
        SELECT Id, CaseNumber, Subject, Status, Priority, CreatedDate,
               Description, Origin
        FROM Case
        ORDER BY CreatedDate DESC
        LIMIT 5
    """
    
    results = sf.query(query)
    
    # Print results
    for record in results['records']:
        print(f"\nCase Number: {record['CaseNumber']}")
        print(f"Subject: {record['Subject']}")
        print(f"Status: {record['Status']}")
        print(f"Priority: {record['Priority']}")
        print(f"Created Date: {record['CreatedDate']}")
        print(f"Origin: {record['Origin']}")
        print("-" * 50)

if __name__ == "__main__":
    get_recent_cases()