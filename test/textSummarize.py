import json
import requests
import os

# Text File Data Array
textArray = []

data = json.load("notion.json")

# Secret token
secret = data["id"]

# Database Id
database = data["database"]

url = "https://api.notion.com/v1/pages"

# Headers
headers = {
    'Authorization': f'Bearer {secret}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16'
}

# Data input
data_input = {
    "parent": { "database_id": f"{database}" },
    "properties": {
    "Name": {
        "title": [
        {
            "text": {
            "content": str(23) 
            }
        }
        ],
        "ders": [
        {
            "multi_select": {
            "content": "Piskoloji" 
            }
        }
        ],
        "content": [
        {
            "text": {
            "content":  "fods" 
            }
        }
        ]
    }
    }
}

# check request 
response = requests.post(url, headers=headers, json=data_input)
print(response.json())