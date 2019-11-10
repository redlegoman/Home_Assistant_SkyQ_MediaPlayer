#!/usr/bin/env python3
import sky_remote
import requests
import sys

# Run ./bash_sky.py <sky_box_ip>
# example: ./bash_sky_test.py 192.168.0.9
# Note: you may need to modify top line change python3 to python, depending on OS/setup. this is works for me on my mac


sky = sky_remote.SkyRemote(sys.argv[1])
print("Sky box power: " + sky.powerStatus())
print(str(sky.getCurrentMedia()))

print("----------- Testing Description 0")
sky._getSoapControlURL(0)
sky._callSkySOAPService('GetTransportInfo')
print(str(sky.getCurrentMedia()))

print("----------- TTesting Description 1")
sky._getSoapControlURL(1)
sky._callSkySOAPService('GetTransportInfo')
print(str(sky.getCurrentMedia()))

print("----------- Testing Description 2")
sky._getSoapControlURL(2)
sky._callSkySOAPService('GetTransportInfo')
print(str(sky.getCurrentMedia()))
