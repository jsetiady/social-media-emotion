import urllib3
import facebook
import requests
import json
import csv
import sys

# You might have to update the token
token= ‘_YOUR_ACCESS_TOKEN’
gojek_id = "166677693366218"
base_url = "https://graph.facebook.com/v2.7/"
graph = facebook.GraphAPI(access_token=token, version = 2.7)

str_comments = []


# Get post id
posts = requests.get(base_url + gojek_id + "/posts?limit=100&access_token="+token) 
posts_json = posts.json()

print posts_json
sys.exit()

for x in range(0, len(posts_json['data'])):
	post_id = posts_json['data'][x]['id']
	comments = requests.get(base_url + post_id + "/comments?limit=100&access_token="+token) 
	comments_json = comments.json()
	for y in range(0, len(comments_json['data'])):
		str_comments.append(comments_json['data'][y]['message'].encode('utf-8'))

feed = requests.get(base_url + gojek_id + "/feed?limit=100&access_token="+token) 
feeds_json = feed.json()

for x in range(0, len(feeds_json['data'])):
	str_comments.append(feeds_json['data'][x]['message'].encode('utf-8'))

# Write to CSV
f = open("test_fb.csv", "wb+")
writer = csv.writer(f)
for item in str_comments:
    writer.writerow([item])