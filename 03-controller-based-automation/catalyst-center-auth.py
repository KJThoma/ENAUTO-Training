import os
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://10.10.20.185/dna/system/api/v1/auth/token"
username = os.environ["CATALYST_USER"]
password = os.environ["CATALYST_PASS"]

auth_request = requests.post(url=auth_url, auth=(username, password), verify=False).json()
print(auth_request['Token'])