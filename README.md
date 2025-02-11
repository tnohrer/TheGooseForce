# TheGooseForce
TheGooseForce is a Salesforce extension for Goose that provides enhanced complaint management capabilities through direct Salesforce integration.

## Features
- **Salesforce API Integration**: Direct connection to your Salesforce org
- **Case Management**: Handle case-related operations using LLMs
- **Automated Workflows**: Execute complex Salesforce operations through simple commands

## Prerequisites
- Python 3.10 or higher
- Salesforce org access
- Goose CLI installed
- Required Python packages (see requirements.txt)
- Must start virtual environment before installing the extension

## Installation

1. Clone the repository:
```
git clone https://github.com/tnohrer/TheGooseForce.git
cd TheGooseForce
```

Create and activate virtual environment:

2. Create virtual environment
```
python -m venv .venv
```

# Activate virtual environment
# Windows:
```
.venv\Scripts\activate
```
# macOS/Linux:
```
source .venv/bin/activate
```
3. Install required packages:

```
pip install -r requirements.txt
```
4. Find your Python and server.py paths:

```
# Get Python path (make sure virtual environment is activated)
which python3

# Verify server.py location
ls -l src/thegooseforce/server.py
```


⚠️ Security Note: This extension currently uses direct login via username, password, and security token. Future versions will implement OAuth2 for enhanced security.

## Goose Extension Setup
To add TheGooseForce to Goose:

###Open Goose
1. Click on the three dots (⋮) in the top right corner
2. Select "Extensions"
3. Click "Add Extension"
4. Fill in the following details:
```
ID: salesforce-mcp
Name: TheGooseForce
Description: Whatever description you want to put. I suggest something funny like "The Goose is loose and it's in Salesforce"
Command: /Users/[username]/Desktop/GooseForce-main/.venv/bin/python3 /Users/[username]/Desktop/GooseForce-main/server.py
```
Replace [username] with your actual username
Note: The command should point to the Python executable in your virtual environment and the server.py file in your installation directory. Make sure to use absolute paths.

5. Setup the needed variables:

```
SALESFORCE_USERNAME: Your Salesforce username
SALESFORCE_PASSWORD: Your Salesforce password
SALESFORCE_SECURITY_TOKEN: Your Salesforce security token
SALESFORCE_INSTANCE_URL: https://test.salesforce.com 
```
Note: These can be changed at any time by clicking the gear icon next to the extension. 

Note: https://test.salesforce.com for a sandbox or https://login.salesforce.com for a production instance. 

After adding the extension:

1. Click "Save"
2. The extension will appear in your extensions list
3. You can now use TheGooseForce capabilities through Goose


##Troubleshooting
Common Setup Issues:

1. Extension Not Loading

```
Verify paths in command are correct and absolute
Check virtual environment is activated
Ensure all requirements are installed
Check logs in Goose developer console (⌘+Option+I)
```

2. Authentication Errors

```
Verify Salesforce credentials in .env file
Check security token is current
Ensure IP address is allowed in Salesforce
Confirm user has API access enabled
```
3. Python Path Issues

```
Use which python3 to verify Python path
Ensure virtual environment is properly activated
Check Python version matches requirements
```
4. Permission Issues

```
Check file permissions on server.py
Verify user has execute permissions on Python
Ensure .env file is readable
```

5. Connection Issues

```
Check internet connectivity
Verify Salesforce org is accessible
Confirm no VPN conflicts
Check for Salesforce maintenance windows
```

Quick Fixes:

Restart Goose after configuration changes
Delete and recreate extension if settings aren't saving
Clear Goose cache if persistent issues occur
Check extension logs for detailed error messages

##Configuration
The extension can be configured through:

Environment variables
.env file
Goose extension settings


##Contributing
This is an open-source project. Contributions, issues, and feature requests are welcome.



##Future Enhancements
OAuth2 implementation
Enhanced security features
Additional Salesforce object support
Expanded query capabilities

