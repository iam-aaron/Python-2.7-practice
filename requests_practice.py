#!/usr/bin/env python  
#we changed this part so it will use the python and packages in the virtual environment

import requests
import argparse
import sys

parser = argparse.ArgumentParser(description='Get the current weather information')
parser.add_argument('--zip', default='45891', help='zip/postal code to get the weather for')
parser.add_argument('--country', default='us', help='country zip/postal belongs to, default is "us"')

args = parser.parse_args()

url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,%s&APPID=%s" % (
    args.zip,
    args.country,
    "15728b4dfb9bb301a8ce735892696e24") #openweathermap API KEY

print(url)

res = requests.get(url)

if res.status_code != 200:
    print("Error talking to weather provider: %s" % res.status_code)
    sys.exit(1)

print(res.json())