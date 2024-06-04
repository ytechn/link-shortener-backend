import requests

url = "http://localhost:7001/api/health_check"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
