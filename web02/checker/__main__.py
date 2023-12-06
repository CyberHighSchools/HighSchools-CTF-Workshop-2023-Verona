import os, requests, re

URL = os.environ.get("URL", "http://change-me.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]
r = requests.post(URL)

try:
    pattern = r'flag\{.*?\}'
    flag = re.findall(pattern, r.text)[0]
except:
    flag = "Not found"

print(flag)