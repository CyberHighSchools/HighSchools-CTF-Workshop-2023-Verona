import os, requests, re

URL = os.environ.get("URL", "http://not-a-robot.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]
r = requests.get(URL + "/pl5_d0nt_vi51t_me")

try:
    pattern = r'flag\{.*?\}'
    flag = re.findall(pattern, r.text)[0]
except:
    flag = "Not found"

print(flag)
