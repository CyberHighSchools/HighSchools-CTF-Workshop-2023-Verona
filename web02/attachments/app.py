import os
from flask import Flask, render_template, request

app = Flask(__name__)

HTTP_PORT = int(os.getenv("HTTP_PORT", 8080))
FLAG = os.getenv("FLAG", "🤓")

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'GET'):
        return render_template('index.html')
    elif(request.method == 'POST'):
        return render_template('flag.html', flag=FLAG)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HTTP_PORT)