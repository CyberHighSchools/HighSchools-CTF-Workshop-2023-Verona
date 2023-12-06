import os, requests, re

URL = os.environ.get("URL", "http://inspect-more.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]
json = {"result": "0.0776"}
r = requests.post(URL + "/validate_result", json=json)

try:
    pattern = r'flag\{.*?\}'
    flag = re.findall(pattern, r.text)[0]
except:
    flag = "Not found"

print(flag)
