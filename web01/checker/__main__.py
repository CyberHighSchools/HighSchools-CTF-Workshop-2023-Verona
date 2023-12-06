import os, requests, re, base64

URL = os.environ.get("URL", "http://cuki.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]
r = base64.b64decode(requests.get(URL).cookies['session']).decode('utf-8')


try:
    pattern = r'flag\{.*?\}'
    flag = re.findall(pattern, r)[0]
except:
    flag = "Not found"

print(flag)