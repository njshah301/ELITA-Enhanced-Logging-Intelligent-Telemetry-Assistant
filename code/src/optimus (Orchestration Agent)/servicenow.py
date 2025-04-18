import requests
from settings import SERVICENOW_INSTANCE, SERVICENOW_USERNAME, SERVICENOW_PASSWORD

def fetch_unassigned_incidents():
    """
    Fetch unassigned incidents from the ServiceNow API.
    """
    url = f"https://{SERVICENOW_INSTANCE}/api/now/table/incident"
    params = {"sysparm_query": "assigned_toISEMPTY"}
    headers = {"Accept": "application/json"}
    response = requests.get(url, auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD), headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("result", [])
    return []

def assign_incident(incident_sys_id, assigned_to):
    """
    Assign an incident to a specific agent in ServiceNow.
    """
    url = f"https://{SERVICENOW_INSTANCE}/api/now/table/incident/{incident_sys_id}"
    payload = {"assigned_to": assigned_to, "state": 2}  # 2 -> Assigned
    headers = {"Content-Type": "application/json"}
    requests.patch(url, auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD), json=payload, headers=headers)


def move_incident_status(incident_sys_id,state):
    """
    Move an incident to 'In Progress' in ServiceNow.
    """
    url = f"https://{SERVICENOW_INSTANCE}/api/now/table/incident/{incident_sys_id}"
    payload = {"state": state}  # 2 -> In Progress
    headers = {"Content-Type": "application/json"}

    response = requests.patch(url, auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD), json=payload, headers=headers)
    return response.json()  

def get_assignment_group(url):
    """
    Retrieve the assignment group name from a given URL.
    """
    response = requests.get(url, auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD), headers={"Accept": "application/json"})
    if response.status_code == 200:
        return response.json().get("result", {}).get("name", "")
    return ""