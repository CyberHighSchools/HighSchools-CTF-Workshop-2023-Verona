import os
from flask import Flask, render_template, request

app = Flask(__name__)

HTTP_PORT = int(os.getenv("HTTP_PORT", 8080))
FLAG = os.getenv("FLAG", "flag{test_flag}")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "ubnt" and password == "ubnt":
            return render_template('flag.html', flag=FLAG)
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HTTP_PORT)