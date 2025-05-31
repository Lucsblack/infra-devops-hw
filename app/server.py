from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return f"""
    <h1>H&W Publishing</h1>
    <p>Server: {hostname}</p>
    <p>Port: {5000 if '5000' in hostname else 5001}</p>
    <style>body {{ font-family: Arial; text-align: center; margin-top: 50px; }}</style>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)