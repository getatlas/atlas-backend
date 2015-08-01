# -*- coding: utf-8 -*-

"""
    citibike.py
    ~~~~~~~~~~~

    A helper class for retrieving citibike data.
"""

import json
import urllib

citibike_url = 'http://www.citibikenyc.com/stations/json'

def update():
    stations = {}
    
    response = urllib.urlopen(citibike_url)
    data = json.loads(response.read())
    retrieved_stations = data['stationBeanList']

    for station in retrieved_stations:
        id = station['id']
        name = station['stationName']
        available = station['availableDocks']
        total = station['totalDocks']
        lat = station['latitude']
        lon = station['longitude']

        stations[id] = {
            'name': name,
            'available': available,
            'total': total,
            'lat': lat,
            'lon': lon
        }

    return stations
