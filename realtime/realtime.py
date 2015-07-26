# -*- coding: utf-8 -*-

from google.transit import gtfs_realtime_pb2 as gtfs
import mta_pb2 as mta
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

    for entity in entities[sys.argv[1]]:
        print entity

    print len(entities[sys.argv[1]])

update()
