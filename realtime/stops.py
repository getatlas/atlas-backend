# -*- coding: utf-8 -*-

import json

def stops():
    f = open('stops.txt', 'r')
    data = f.read()

    lines = data.split('\n')
    stops = {}

    first = False

    for line in lines:
        if first == False:
            first = True
            continue

        stopdata = line.split(',')

        if len(stopdata) > 1:
            stops[stopdata[0]] = {
                'stop_name': stopdata[2],
                'stop_lat': stopdata[4],
                'stop_lon': stopdata[5]
            }

    return stops
