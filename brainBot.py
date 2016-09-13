#!/usr/bin/env python

import requests
import random
from datetime import datetime
from dateutil import tz

def brainShop(msg)
    url = 'http://api.brainshop.ai/get'
    querystring = {"bid":"303","key":"UMVEIqUn9ncSty88","uid":"100","msg":msg}
    
    headers = {
        'cache-control': "no-cache"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    dump = response.json()
    
    brainbot_response =  dump['cnt']

    return brainbot_response


def chuckNorris()
    url = "http://api.icndb.com/jokes/random"
    
    headers = {
        'cache-control': "no-cache"
            }
    
    response = requests.request("GET", url, headers=headers)
    
    dump = response.json()
    
    chucknorris_response = dump['value']['joke']
    return chucknorris_response
    
def gifyMeme(search)
    search_param = search
    url = "http://api.giphy.com/v1/gifs/search"
    
    querystring = {"q":search_param,"api_key":"dc6zaTOxFJmzC"}
    
    headers = {
        'cache-control': "no-cache"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    dump = response.json()
    if len(dump['data']) >= 5:
        randInt = random.randint(0, 5)
    elif len(dump['data']) <= 2:
        randInt = 0
    else:
        randInt = int(random.randint(0, len(dump['data'])))
    print randInt
    
    giffy_response=dump['data'][randInt]['url']
    giffy_rating=dump['data'][randInt]['rating']
    if giffy_rating == 'r':
        giffy_response = 'Sorry this one is not safe for work. Nice try!'
    
    return giffy_response


def sunInfo()
    url = "http://api.sunrise-sunset.org/json"
    
    querystring = {"lat":"41.681111","lng":" -72.940556","date":"today"}
    
    headers = {
        'cache-control': "no-cache"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    dump = response.json()
    sunrise = dump['results']['sunrise']
    sunset = dump['results']['sunset']
    day_length = dump['results']['day_length']
    
    
    sunrise = sunrise[:8]
    sunset = sunset[:8]
    
    # METHOD 1: Hardcode zones:
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/New_York')
    
    # utc = datetime.utcnow()
    sunrise_utc = datetime.strptime(sunrise, '%H:%M:%S')
    sunset_utc = datetime.strptime(sunset, '%H:%M:%S')
    
    # Tell the datetime object that it's in UTC time zone since
    # datetime objects are 'naive' by default
    sunrise_utc = sunrise_utc.replace(tzinfo=from_zone)
    sunset_utc = sunset_utc.replace(tzinfo=from_zone)
    # Convert time zone
    sunset_est = sunset_utc.astimezone(to_zone)
    sunrise_est = sunrise_utc.astimezone(to_zone)
    return "Sunrise: "+str(sunrise_est)[11:-6]+" am"+ "Sunset: "+str(sunset_est)[11:-6]+" pm"+"Length of day: "+day_length

#usage
msg = "hello world"
print brainShop(msg)
print chuckNorris()
search = "Chuck Norris"
print gifyMeme(search)
print sunInfo()
