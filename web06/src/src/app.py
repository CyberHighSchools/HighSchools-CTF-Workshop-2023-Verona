import os
from flask import Flask, jsonify, render_template, request, send_from_directory

app = Flask(__name__, static_folder='static')

HTTP_PORT = int(os.getenv("HTTP_PORT", 8080))
FLAG = os.getenv("FLAG", "flag{test_flag}")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/pl5_d0nt_vi51t_me')
def hidden():
    return render_template("flag.html", flag=FLAG)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HTTP_PORT)