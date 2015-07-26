# -*- coding: utf-8 -*-

from google.transit import gtfs_realtime_pb2 as gtfs
import mta_pb2 as mta
import stops
import sys
import urllib

mta_url = 'http://datamine.mta.info/files/k38dkwh992dk/gtfs'

def update():
    response = urllib.urlopen(mta_url)

    feed = gtfs.FeedMessage()
    feed.ParseFromString(response.read())

    entities = {}

    for entity in feed.entity:
        if entity.HasField('vehicle'):
            route_id = entity.vehicle.trip.route_id
            if route_id in entities.keys():
                entities[route_id].append(entity)
            else:
                entities[route_id] = [entity]

    train = "4"

    trains = {}

    for entity in entities[train]:
        # print entity

        trains[entity.id] = {
            'lat': stops.stops()[entity.vehicle.stop_id]['stop_lat'],
            'lon': stops.stops()[entity.vehicle.stop_id]['stop_lon']
        }

        print trains[entity.id]

    print len(entities[train])

update()
