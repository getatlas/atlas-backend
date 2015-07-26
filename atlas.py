# -*- coding: utf-8 -*-

"""
    Atlas
    ~~~~~

    The best mapping app the world has ever seen.
"""

from flask import Flask
import realtime
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi there'

@app.route('/shapes')
def shapes():
    f = open('shapes.txt', 'r')
    data = f.read()
    for line in data.split('\n'):
        print line
    return 'hi'

def update_realtime():
    feed = gtfs.FeedMessage()
    response = urllib.urlopen('http://datamine.mta.info/files/k38dkwh992dk/gtfs')
    feed.ParseFromString(response.read())

    for entity in feed.entity:
        if entity.HasField('trip_update'):
            print entity.trip_update

    threading.Timer(60, update_realtime).start()

if __name__ == '__main__':
    update_realtime()
    app.run()
