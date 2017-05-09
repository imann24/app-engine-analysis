# Author: Isaiah Mann
# Description: Tests the average response time of a given website across a specified number of requests
# Usage: python main.py [web page URL] [number of requests] [OPTIONAL: wait time between each request]

import sys
import requests
from time import sleep

webPageURL = sys.argv[1]
timesToRun = int(sys.argv[2])
if(len(sys.argv) > 3):
    waitBetweenRequest = float(sys.argv[3])
else:
    waitBetweenRequest = False;
sum = 0
for n in range(timesToRun):
    sum += requests.get(webPageURL).elapsed.total_seconds()
    if(waitBetweenRequest):
        sleep(waitBetweenRequest)
avg = sum / timesToRun
print("%d,%.2f" % (timesToRun, avg))
