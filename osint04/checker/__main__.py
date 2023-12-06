#!/usr/bin/env python3

import requests
import json
import re

ONION = "cybrmnksohq46mrky5oqrkj4zp4l7uq4zy5w54ih3crvu3lczi6xfeid.onion"
proxies = {
    'http': 'socks5h://0.0.0.0:8050',
    'https': 'socks5h://0.0.0.0:8050'
}

print(f"[*] checking if http://{ONION}/ is up...")
r = requests.get(f"http://{ONION}/breaches/iotinga.IT/breach-preview.txt", proxies=proxies)
try:
    pattern = r'flag\{.*\}'
    flag = re.findall(pattern, r.text)[0]
except:
    flag = "Not found"

print(flag)
