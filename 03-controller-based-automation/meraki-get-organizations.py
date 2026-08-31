import os
import requests
from dotenv import load_dotenv
from rich import print

load_dotenv()

MERAKI_KEY = os.environ["MERAKI_KEY"]
ORG_URL = "https://api.meraki.com/api/v1/organizations/"

headers = {
    "Authorization": f"Bearer {MERAKI_KEY}"
}

response = requests.get(url=ORG_URL, headers=headers).json()
print(response)