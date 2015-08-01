# -*- coding: utf-8 -*-

"""
    Atlas
    ~~~~~

    The best mapping app the world has ever seen.
"""

from flask import Flask
import os
# import realtime.realtime as realtime
import subway
import threading
import urllib2

# Rewrite this in actual python sometime soon
# os.system("""cd ./subway\
# && rm -rf google_transit*\
# && mkdir google_transit\
# && cd google_transit\
# && wget http://web.mta.info/developers/data/nyct/subway/google_transit.zip\
# && unzip google_transit.zip""")

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi there'

def update():
    subway.update()
    threading.Timer(10, update).start()

if __name__ == '__main__':
    # update()
    subway.update()
    # app.run()
