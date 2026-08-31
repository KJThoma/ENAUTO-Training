import requests
import urllib3
from rich import print
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://10.10.20.185/dna/system/api/v1/auth/token"
deployments_url = "https://10.10.20.185/dna/intent/api/v1/icapSettings/deviceDeployments"
username = os.environ["CATALYST_USER"]
password = os.environ["CATALYST_PASS"]


auth_request = requests.post(url=auth_url, auth=(username, password), verify=False).json()
my_token = auth_request["Token"]

headers = {
    "x-auth-token": my_token,
    "Accept": "application/json"
}

deployments_request = requests.get(url=deployments_url, headers=headers, verify=False).json()
print(deployments_request)