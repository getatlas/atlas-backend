# -*- coding: utf-8 -*-

"""
    wifi.py
    ~~~~~~~

    A helper class for retrieving data about public wifi
    hotspots.
"""

from bs4 import BeautifulSoup
import re
import urllib

hotspots_url = 'https://nycopendata.socrata.com/api/geospatial/a9we-mtpn?method=export&format=KML'

def update():
    hotspots = {}

    response = urllib.urlopen(hotspots_url)

    soup = BeautifulSoup(response.read(), 'lxml-xml')
    retrieved_hotspots = soup.find_all('Placemark')

    for hotspot in retrieved_hotspots:
        id = hotspot['id']

        description = hotspot.description.contents[0]
        type = re.search('<li><strong><span class="atr-name">Type</span>:</strong> <span class="atr-value">(.*)</span></li>', description).group(1)
        provider = re.search('<li><strong><span class="atr-name">Provider</span>:</strong> <span class="atr-value">(.*)</span></li>', description).group(1)

        lat = float(hotspot.LookAt.latitude.contents[0])
        lon = float(hotspot.LookAt.longitude.contents[0])

        hotspots[id] = {
            'type': type,
            'provider': provider,
            'lat': lat,
            'lon': lon
        }

    return hotspots
