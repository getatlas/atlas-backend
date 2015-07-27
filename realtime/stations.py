# -*- coding: utf-8 -*-

stations = {}

class Station(object):

    def __init__(self, line):
        data = line.split(',')
        id = data[0]

        self.name = data[2]
        self.lat = data[4]
        self.lon = data[5]

def load_stations():
    f = open('stops.txt', 'r')
    contents = f.read()

    for line in contents.split('\n'):
        data = line.split(',')
        id = data[0]

        if id.endswith('N') or id.endswith('S'):
            continue

        station = Station(line)
        stations[id] = station

def get_station(id):
    if len(stations) == 0:
        load_stations()

    return stations[id]
