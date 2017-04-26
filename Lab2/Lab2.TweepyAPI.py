#!/usr/bin/env python
import sys
import tweepy
from tweepy import OAuthHandler
import json

#Alternative style of handing over the secret keys:
#Call the python script directly with bash variables.
#./Lab2.TweepyAPI.py <consumer-key> <consumer-secret> <access-token> <access-secret>
#Then you can retrieve the secret keys from the argument list.
consumer_key = sys.argv[0]
consumer_secret = sys.argv[1]
access_token = sys.argv[2]
access_secret = sys.argv[3]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.followers_count))
print('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))

#for status in tweepy.Cursor(api.home_timeline).items(1):
#    print(json.dumps(status._json, indent=2))

