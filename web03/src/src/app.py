import os
from flask import Flask, render_template, request

app = Flask(__name__)

HTTP_PORT = int(os.getenv("HTTP_PORT", 8080))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/menu')
def exec_cmd():
    file_path = request.args.get('file')
    if file_path:
        try:
            with open(file_path, 'r') as file:
                return render_template("menu.html", file_content=file.read())
        except FileNotFoundError:
            return "File not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HTTP_PORT)