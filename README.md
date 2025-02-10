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

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tnohrer/TheGooseForce.git
cd TheGooseForce
Install required packages:

pip install -r requirements.txt
Configure your Salesforce credentials in .env file:

SALESFORCE_USERNAME=your_username
SALESFORCE_PASSWORD=your_password
SALESFORCE_SECURITY_TOKEN=your_security_token
⚠️ Security Note: This extension currently uses direct login via username, password, and security token. Future versions will implement OAuth2 for enhanced security.

Goose Extension Setup
To add TheGooseForce to Goose:

Open Goose
Click on the three dots (⋮) in the top right corner
Select "Extensions"
Click "Add Extension"
Fill in the following details:
ID: salesforce-mcp
Name: TheGooseForce
Description: Salesforce integration for complaint and case management
Command: /Users/[username]/Desktop/GooseForce-main/.venv/bin/python3 /Users/[username]/Desktop/GooseForce-main/server.py
Replace [username] with your actual username
Note: The command should point to the Python executable in your virtual environment and the server.py file in your installation directory. Make sure to use absolute paths.

After adding the extension:

Click "Save"
The extension will appear in your extensions list
You can now use TheGooseForce capabilities through Goose
Troubleshooting
Common Setup Issues:

Extension Not Loading

Verify paths in command are correct and absolute
Check virtual environment is activated
Ensure all requirements are installed
Check logs in Goose developer console (⌘+Option+I)
Authentication Errors

Verify Salesforce credentials in .env file
Check security token is current
Ensure IP address is allowed in Salesforce
Confirm user has API access enabled
Python Path Issues

Use which python3 to verify Python path
Ensure virtual environment is properly activated
Check Python version matches requirements
Permission Issues

Check file permissions on server.py
Verify user has execute permissions on Python
Ensure .env file is readable
Connection Issues

Check internet connectivity
Verify Salesforce org is accessible
Confirm no VPN conflicts
Check for Salesforce maintenance windows
Quick Fixes:

Restart Goose after configuration changes
Delete and recreate extension if settings aren't saving
Clear Goose cache if persistent issues occur
Check extension logs for detailed error messages
Configuration
The extension can be configured through:

Environment variables
.env file
Goose extension settings
Contributing
This is an open-source project. Contributions, issues, and feature requests are welcome.

License
MIT License

Future Enhancements
OAuth2 implementation
Enhanced security features
Additional Salesforce object support
Expanded query capabilities
