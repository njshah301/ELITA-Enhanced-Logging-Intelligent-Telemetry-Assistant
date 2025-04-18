


import base64
import sys
import os
from dotenv import load_dotenv
import requests
import json
import logging


logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

sys.stdout.reconfigure(encoding="utf-8")

# GitHub Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Set in .env file
REPO_OWNER = "firaz-bug"
REPO_NAME = "global-hackathon"
FILE_PATH = "sample.txt"  # The path inside the repo
COMMIT_MESSAGE = "Automated update via Django API"

# GitHub API URL for the file
GITHUB_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def get_file_sha():
    """Fetches the SHA of the file required for updating."""
    response = requests.get(GITHUB_API_URL, headers=HEADERS)
    if response.status_code == 200:
        sha = response.json().get("sha")
        logger.info("SHA fetched successfully: %s", sha)
        return sha
    elif response.status_code == 404:
        logger.error("File not found. Ensure the path is correct.")
        return None
    else:
        logger.error("Error fetching file: %s", response.json())
        return None

def update_github_file(new_content):
    """Updates the file on GitHub with new content."""
    sha = get_file_sha()
    if not sha:
        return

    # Properly encode the new content in Base64
    encoded_content = base64.b64encode(new_content.encode()).decode()
    logger.info("Encoded content successfully.")

    data = {
        "message": COMMIT_MESSAGE,
        "content": encoded_content,
        "sha": sha,  # Required for updating an existing file
    }

    response = requests.put(GITHUB_API_URL, headers=HEADERS, data=json.dumps(data))
    
    if response.status_code in [200, 201]:
        logger.info("File updated successfully!")
    else:
        logger.error("Error updating file: %s", response.json())

if __name__ == "__main__":
    new_content = "Updated content for the file via Django API."
    update_github_file(new_content)
