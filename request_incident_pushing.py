import requests
import json

url = "http://172.10.0.228/webservices/rest.php?version=1.3&json_data=%s"
username = "username here"
password = "password here"

json_data = {
    "operation": "core/create",
    "comment": "Ticket created",
    "class": "UserRequest", # UserRequest / Incident
    "fields":    {
        "org_id": "SELECT Organization WHERE id = <YOUR ORG ID>", 
        "service_id": "SELECT Service WHERE id = <YOUR SERVICE ID>",
        "servicesubcategory_id": "SELECT ServiceSubcategory WHERE id = <YOUR SUBCATEGORY SERVICE ID>",
        "impact": 1, # 1: department, 2: service, 3: person
        "urgency": 1, # 1: critical, 2: high, 3: medium, 4: low
        "caller_id":
        {
            "name": "your name here",
            "first_name": "your first name here",
        },
        "title": "TITLE",
        "description": "DESCRIPTION"        
    }
}


url = "http://<your itop portal>/webservices/rest.php?version=1.3&json_data=%s" % str(json_data).replace("'", "\"")

response = requests.post(url, auth=(username, password))

if response.status_code == 200:
    result = json.loads(response.text)
    if "code" in result and result["code"] == 0:
        print("Ticket created sucessfully")
    else:
        print(result["message"])
else:
    print("Connection error:", response.status_code)
