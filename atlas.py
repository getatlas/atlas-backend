# -*- coding: utf-8 -*-

"""
    Atlas
    ~~~~~

    The best mapping app the world has ever seen.
"""

from flask import Flask
import realtime.realtime as realtime
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi there'

def update_realtime():
    realtime.update()
    threading.Timer(5, update_realtime).start()

if __name__ == '__main__':
    update_realtime()
    # app.run()
