'''Lab Practical 13
Problem Statement:
Study of ThingSpeak – an API and Web Service for the Internet of Things (Mini 
Project: Same can be done parallel with PBL)'''

import requests
import time
import random
channel_id = 394744 # PUT CHANNEL ID HERE
write_key = 'AAOG612RJT5LW21R' # PUT YOUR WRITE KEY HERE
read_key = 'TSPKJB230K65QPJQ' # PUT YOUR READ KEY HERE
if __name__ == "__main__":
 while True:
         val = random.randint(0,99)
         #print(val)
         URL = 'http://api.thingspeak.com/update?api_key=%s&field1=%s'%(write_key,val)
         #print(URL)
         resp = requests.get(url=URL)
          #print(resp.json())
         # free account has an api limit of 15sec
         time.sleep(30)


import requests
import json
import time
Key = 'TSPKJB230K65QPJQ'
channel = 394744
while True:
    try:
#URL = 'http://api.thingspeak.com/channels/%s/feeds/last.json?' %(channel)
         URL = 'http://api.thingspeak.com/channels/%s/field/1' %(channel)
#print(URL)
         resp = requests.get(url=URL)
#print(resp)
         resp = resp.json()['feeds'][-1]['field1']
         print(resp)
         time.sleep(0.3)
    except KeyboardInterrupt:
        exit()