import os
from flask import Flask, render_template, make_response
import base64

app = Flask(__name__)

HTTP_PORT = int(os.getenv("HTTP_PORT", 8080))
FLAG = os.getenv("FLAG", "flag{test_flag}")

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('session', base64.b64encode(FLAG.encode('utf-8')).decode('utf-8'), httponly=True, secure=True)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HTTP_PORT)