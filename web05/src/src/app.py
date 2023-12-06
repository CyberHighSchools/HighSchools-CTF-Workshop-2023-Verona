import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

HTTP_PORT = int(os.getenv("HTTP_PORT", 8080))
FLAG = os.getenv("FLAG", "flag{test_flag}")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/validate_result', methods=['POST'])
def validate_result():
    data = request.get_json()
    inputResult = float(data["result"])

    if inputResult == 0.0776:
        return jsonify({'success': 1,'message': 'Corretto! Ecco la tua flag: ' + FLAG})
    else:
        return jsonify({'success': 0, 'message': 'Sbagliato! Riprova.'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HTTP_PORT)