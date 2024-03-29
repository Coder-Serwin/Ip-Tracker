from flask import Flask, request
from bot import *
import os

D_TOKEN = os.getenv('D_TOKEN')
os.environ['IP_ADDR'] = "None"
app = Flask(__name__)
ip_address = None

@app.route('/')
def home():
    ip_address = request.remote_addr
    os.environ['IP_ADDR'] = ip_address
    client.run(D_TOKEN)
    return f"{ip_address}"

if __name__ == '__main__':
    app.run(debug=True)