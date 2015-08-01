# -*- coding: utf-8 -*-

"""
    hurricane.py
    ~~~~~~~~~~~~

    A helper class for retrieving data about hurricane
    evacuation centers.
"""

from bs4 import BeautifulSoup
import re
import urllib

stormcenters_url = 'https://nycopendata.socrata.com/api/geospatial/ayer-cga7?method=export&format=KML'

def update():
    centers = {}

    response = urllib.urlopen(stormcenters_url)

    soup = BeautifulSoup(response.read(), 'lxml-xml')
    retrieved_centers = soup.find_all('Placemark')

    for center in retrieved_centers:
        id = center['id']

        description = center.description.contents[0]
        name = re.search('<li><strong><span class="atr-name">EC_NAME</span>:</strong> <span class="atr-value">(.*)</span></li>', description).group(1)
        address = re.search('<li><strong><span class="atr-name">ADDRESS</span>:</strong> <span class="atr-value">(.*)</span></li>', description).group(1)
        zip = int(re.search('<li><strong><span class="atr-name">ZIP_CODE</span>:</strong> <span class="atr-value">(.*).0</span></li>', description).group(1))

        lat = float(center.LookAt.latitude.contents[0])
        lon = float(center.LookAt.longitude.contents[0])

        centers[id] = {
            'name': name,
            'address': address,
            'zip': zip,
            'lat': lat,
            'lon': lon
        }

    return centers
