from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    port = os.environ.get("PORT", 5000)
    return f'Hello from H&W! Running on port {port}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))