# -*- coding: utf-8 -*-

"""
    shape.py
    ~~~~~~~~~~

    Helper file for retrieving and returning data
    about MTA subway paths.
"""

import station

_shapes = {}

class Shape(object):

    def __init__(self, path):
        self.path = path


# Parses CSV from shapes.txt and saves it in memory

def load_shapes():
    f = open('./subway/google_transit/shapes.txt', 'r')
    contents = f.read()

    path = []
    shapeid = ''

    i = -1

    for line in contents.split('\n'):
        data = line.split(',')

        i += 1

        if len(data) < 4 or i == 0:
            continue

        if data[3] == '0' and i > 1:
            shape = Shape(path)
            _shapes[shapeid] = shape

            path = []
        else:
            if i == 0:
                continue

            shapeid = data[0]
            path.append([data[1], data[2]])


# Provides a more public method of retrieving a shape

def get_shape(id):
    if len(_shapes) == 0:
        load_shapes()

    if id in _shapes.keys():
        return _shapes[id]
