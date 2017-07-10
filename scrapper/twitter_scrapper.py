import re
import tweepy 
import json
from tweepy import OAuthHandler
 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

print "["

def process_or_store(tweet):
    tweet = json.dumps(tweet)
    tweet = re.sub(r"\\u(.){4}", " ", tweet)
    print tweet
    print ", "

#for tweet in tweepy.Cursor(api.user_timeline).items():
#    process_or_store(tweet._json)
'''
for tweet in tweepy.Cursor(api.search, q="gojek OR go-jek \
	OR gopay OR go-pay OR goclean OR go-clean \
	gofood OR go-food OR goride OR go-ride \
	gocar OR go-car OR gosend OR go-send").items():
    process_or_store(tweet._json)
'''


for tweet in tweepy.Cursor(api.search, q="gojek OR go-jek").items():
    process_or_store(tweet._json)

print "]"
'''
for tweet in tweepy.Cursor(api.search, q="gopay OR go-pay").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="goclean OR go-clean").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="gofood OR go-food").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="goride OR go-ride").items():
    process_or_store(tweet._json)
'''
'''
for tweet in tweepy.Cursor(api.search, q="gocar OR go-car").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="gosend OR go-send").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="gopulsa OR go-pulsa").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="goshop OR go-shop").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="gomart OR go-mart").items():
    process_or_store(tweet._json)    

for tweet in tweepy.Cursor(api.search, q="gotix OR go-tix").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="gobox OR go-box").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="gomassage OR go-massage").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="goglam OR go-glam").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="goclean OR go-clean").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="goauto OR go-auto").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="gomed OR go-med").items():
    process_or_store(tweet._json)

for tweet in tweepy.Cursor(api.search, q="gobusway OR go-busway").items():
    process_or_store(tweet._json)
'''
