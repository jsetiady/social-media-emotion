import re, tweepy, json, csv, sys, time
from tweepy import OAuthHandler
 
consumer_key = '_YOUR_CONSUMER_KEY_'
consumer_secret = '_YOUR_CONSUMER_SECRET_'
access_token = '_YOUR_ACCESS_TOKEN_'
access_secret = '_YOUR_ACCESS_SECRET_'

csv_filename = "twitter.csv"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError:
            print "sleep"
            time.sleep(15 * 60)



f = open(csv_filename, "wb+")
writer = csv.writer(f)

for tweet in limit_handled(tweepy.Cursor(api.search, q="gojek OR go-jek OR @gojekindonesia").items()):
    t = tweet._json
    t = json.dumps(t["text"])
    t = re.sub(r"\\u(.){4}", " ", t) # remove unicode character
    t = re.sub(r"http(.)*?(\s|$)", "", t) # remove url / link
    t = re.sub(r"\s\s+", " ", t) # remove multi-space
    print t
    # Write to CSV
    writer.writerow([t])

