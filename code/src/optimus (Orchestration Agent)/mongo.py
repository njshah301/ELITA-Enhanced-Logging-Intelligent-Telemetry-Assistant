from pymongo import MongoClient
from settings import MONGO_URI
from datetime import datetime

def get_agent_details(assignment_group):
    """
    Retrieve agent details for a given assignment group from MongoDB.
    """
    client = MongoClient(MONGO_URI)
    db = client["platformManager"]
    collection = db["assignmentGroup"]
    assignment_doc = collection.find_one({"_id": "assignment_mapping"})
    if assignment_doc:
        return assignment_doc["mappings"].get(assignment_group, {})
    return {}


def getLogs(startTime,endTime):
    """
    Retrieve logs from MongoDB within a given time range.
    """
    client = MongoClient(MONGO_URI)
    db = client["platformManager"]
    collection = db["logs"]
    return collection.find({"timestamp": {"$gte": startTime, "$lte": endTime}})
def getPlatformOwner(assignment_group):
    """
    Retrieve platformOwner for a given assignment group from MongoDB.
    """
    client = MongoClient(MONGO_URI)
    db = client["platformManager"]
    collection = db["assignmentGroup"]
    assignment_doc = collection.find_one({"_id": "assignment_mapping"})
    if assignment_doc:
        return assignment_doc["mappings"].get(assignment_group, {})
    return {}

start_time = datetime(2024, 3, 1, 0, 0, 0)  # March 1, 2025, 00:00:00
end_time = datetime(2025, 4, 23, 23, 59, 59)  # March 23, 2025, 23:59:59

logs=getLogs(start_time,end_time)

for log in logs:
    print(log)
