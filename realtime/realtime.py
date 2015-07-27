# -*- coding: utf-8 -*-

from google.transit import gtfs_realtime_pb2 as gtfs
import mta_pb2 as mta
import station
import sys
from train import Train
import urllib

mta_url = 'http://datamine.mta.info/files/k38dkwh992dk/gtfs'

def update():
    response = urllib.urlopen(mta_url)

    feed = gtfs.FeedMessage()
    feed.ParseFromString(response.read())

    entities = []

    for entity in feed.entity:
        if entity.HasField('vehicle'):
            train = Train(entity)
            print train.id

update()
