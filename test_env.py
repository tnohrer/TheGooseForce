from dotenv import load_dotenv
import os

load_dotenv()

print("Username:", os.getenv("SALESFORCE_USERNAME"))
print("Password:", "***" if os.getenv("SALESFORCE_PASSWORD") else "Not found")
print("Token:", "***" if os.getenv("SALESFORCE_SECURITY_TOKEN") else "Not found")