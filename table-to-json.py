#!/usr/bin/python
import json
import sys

if __name__ == '__main__':
    coords = []
    center=250
    maxnum = 50
    count = 0
    scale = int(sys.argv[2])
    with open(sys.argv[1]) as inf:
        for line in inf:
            if count < maxnum:
                lat, lng = line.split()
                lat = float(lat)
                lng = float(lng)
                lat = lat - center
                lng = lng - center
                lat = lat / scale
                lng = lng / scale
                coords.append(dict(lat=lat, lng=lng))
            count += 1
    print "myCoords = " + json.dumps(coords)
