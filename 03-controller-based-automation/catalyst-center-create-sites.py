import os
import requests
import urllib3
from dotenv import load_dotenv
from rich import print

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://10.10.20.185/dna/system/api/v1/auth/token"
site_url = "https://10.10.20.185/dna/intent/api/v1/site"
username = os.environ["CATALYST_USER"]
password = os.environ["CATALYST_PASS"]


auth_request = requests.post(url=auth_url, auth=(username, password), verify=False).json()
my_token = auth_request["Token"]

headers = {
    "x-auth-token": my_token,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

payload = {
    "type": "area",
    "site": {
        "area": {
            "name": "Italia",
            "parentName": "Global"
        }
    }
}

site_request = requests.post(url=site_url, headers=headers, json=payload, verify=False)
print(site_request.text)