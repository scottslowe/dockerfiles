#!/usr/bin/env python

from flask import Flask
from flask import render_template
from flask import request
from flask import Response
import socket
import datetime

__author__ = 'slowe'

app = Flask(__name__)

HOSTNAME = socket.gethostname()
LOCALADDR = socket.gethostbyname(socket.gethostname())

@app.route("/")
@app.route("/index")
def hello():

    host = {'hostname': HOSTNAME, 'ip': LOCALADDR}
    time = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")
    client = request.remote_addr
    baseurl = request.base_url
    urlroot = request.url_root
    return render_template('index.html', title='Home', host=host, client=client, baseurl=baseurl, urlroot=urlroot, time=time, )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=True, port=5000)
