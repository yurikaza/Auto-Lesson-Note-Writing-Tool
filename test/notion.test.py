import json
import requests

jsonFile = open("notion.json")

data = json.load(jsonFile)

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

data_input = {
    "parent": { "database_id": f"{database}" },
    "properties": {
        "Dakika": {
            "title": [
                {
                    "text": {
                        "content": "2"
                    }
                }
            ]
        },
        "Ders": {
            "multi_select": [{"name": "Piskoloji"}]                    
        }   
    }
}

# check request 
response = requests.post(url, headers=headers, json=data_input)
print(response.json())