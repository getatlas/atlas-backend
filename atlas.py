# -*- coding: utf-8 -*-

"""
    Atlas
    ~~~~~

    The best mapping app the world has ever seen.
"""

import citibike
import flask
from flask import Flask, Response
import json
import os
import hurricane
import subway
import sqlite3
import threading
import urllib2
import wifi

# Rewrite this in actual python sometime soon
# os.system("""cd ./subway\
# && rm -rf google_transit*\
# && mkdir google_transit\
# && cd google_transit\
# && wget http://web.mta.info/developers/data/nyct/subway/google_transit.zip\
# && unzip google_transit.zip""")

stormcenters = {}
bikestations = {}
wifihotspots = {}
places = {}

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi there'

@app.route('/bikes')
def get_bikes():
    global bikestations
    return Response(json.dumps(bikestations), mimetype='application/json')

@app.route('/places')
def get_places():
    global places
    return Response(json.dumps(places), mimetype='application/json')

@app.route('/stormcenters')
def get_stormcenters():
    global stormcenters
    return Response(json.dumps(stormcenters), mimetype='application/json')

@app.route('/wifi')
def get_wifi():
    global wifihotspots
    return Response(json.dumps(wifihotspots), mimetype='application/json')

@app.errorhandler(500)
def internal_server_error(e):
    return flask.jsonify(error=500, text=str(e)), 500

def update():
    global stations
    bikestations = citibike.update()
    threading.Timer(10, update).start()

if __name__ == '__main__':
    # update()
    bikestations = citibike.update()
    stormcenters = hurricane.update()
    wifihotspots = wifi.update()

    objects = sqlite3.connect('data.db').execute('select * from places order by id desc')
    places = [dict(id=row[0], name=row[1], latitude=row[2], longitude=row[3]) for row in objects.fetchall()]

    app.run(debug=True)
