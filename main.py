# Author: Isaiah Mann
# Description: Tests the response time of a given website

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
print("Average Response Time %.2f" % (avg))
