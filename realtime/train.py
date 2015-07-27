# -*- coding: utf-8 -*-

"""
    train.py
    ~~~~~~~~

    Helper class used to simplify parsing of MTA
    data.
"""

from google.transit import gtfs_realtime_pb2 as gtfs
import station

class Train(object):

    def __init__(self, entity):
        self.id = entity.id
        self.line = entity.vehicle.trip.route_id
        self.status = entity.vehicle.current_status
        self.timestamp = entity.vehicle.timestamp
        self.stop = station.get_station(entity.vehicle.stop_id[:-1])
