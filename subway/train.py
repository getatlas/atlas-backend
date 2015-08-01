# -*- coding: utf-8 -*-

"""
    train.py
    ~~~~~~~~

    Helper class used to simplify parsing of MTA
    data.
"""

from google.transit import gtfs_realtime_pb2 as gtfs
import shape
import station

class Train(object):

    def __init__(self, entity):
        self.id = entity.vehicle.trip.trip_id
        self.line = entity.vehicle.trip.route_id
        self.shapeid = entity.vehicle.trip.trip_id.split('_')[1]

        self.status = entity.vehicle.current_status
        self.timestampe = entity.vehicle.timestamp
        self.stations = [station.get_station(entity.vehicle.stop_id[:-1])]

    def update(self, entity):
        self.status = entity.vehicle.current_status
        self.timestampe = entity.vehicle.timestamp
        
        s = station.get_station(entity.vehicle.stop_id[:-1])
        if s not in self.stations:
            self.stations.append(s)
