#!/usr/bin/env python3
import sky_remote
import sys

sky = sky_remote.SkyRemote(sys.argv[1])
sky.press(sys.argv[2])
