#!/usr/bin/python
# A http server, host and custom port - hardcoded

import os
import sys
import time
import signal

from flask import Flask


APP=Flask(__name__)

@APP.route("/")
def index():
    return "HTTP Verification Server"

def doit():
    APP.run(host="50.50.10.11", port=5000)

if __name__ == "__main__":
        signal.signal(signal.SIGHUP, signal.SIG_IGN)
        pid = os.fork()
        if not pid:
            doit()
