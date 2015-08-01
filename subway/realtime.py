# -*- coding: utf-8 -*-

from google.transit import gtfs_realtime_pb2 as gtfs
import sys
from train import Train
import urllib

mta_url = 'http://datamine.mta.info/files/k38dkwh992dk/gtfs'

trains = {}

def update():
    response = urllib.urlopen(mta_url)

    feed = gtfs.FeedMessage()
    feed.ParseFromString(response.read())

    entities = []

    for entity in feed.entity:
        if entity.HasField('vehicle'):
            train = Train(entity)

            if train.id in trains.keys():
                trains[train.id].update(entity)

                train = trains[train.id]
                station = train.stations[-1]

                if train.id == '121550_4..N06R':
                    status = 'incoming at'

                    if train.status == 1:
                        status = 'stopped at'
                    elif train.status == 2:
                        status = 'in transit to'

                    print 'The %s train is %s %s' % (train.line, status, station.name)
            else:
                trains[train.id] = train
