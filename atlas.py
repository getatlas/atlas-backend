# -*- coding: utf-8 -*-
"""
    Atlas
    ~~~~~

    The best mapping app the world has ever seen.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi there'

if __name__ == '__main__':
    app.run()
