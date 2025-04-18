import os
from dotenv import load_dotenv


load_dotenv()
# MongoDB URI
MONGO_URI = os.getenv("MONGO_URI")

# ServiceNow credentials
SERVICENOW_INSTANCE = os.getenv("SERVICENOW_INSTANCE")
SERVICENOW_USERNAME = os.getenv("SERVICENOW_USERNAME")
SERVICENOW_PASSWORD = os.getenv("SERVICENOW_PASSWORD")