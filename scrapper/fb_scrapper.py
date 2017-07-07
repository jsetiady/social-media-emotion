import urllib3
import facebook
import requests
import json
import csv
import sys

# You might have to update the token
token= '_YOUR_ACCESS_TOKEN_'
gojek_id = "166677693366218"
base_url = "https://graph.facebook.com/v2.7/"
graph = facebook.GraphAPI(access_token=token, version = 2.7)

str_comments = []

posts_next_page = base_url + gojek_id + "/posts?limit=100&access_token="+token

while posts_next_page != "":
	posts = requests.get(posts_next_page) 
	posts_json = posts.json()
	print "posts"

    # Get post id
	for x in range(0, len(posts_json['data'])):
		post_id = posts_json['data'][x]['id']

		comments_next_page = base_url + post_id + "/comments?limit=100&access_token="+token
		comments = requests.get(comments_next_page)
		comments_json = comments.json()
		print "comments " + str(x)
		if comments_json.has_key('data'):
			for y in range(0, len(comments_json['data'])):
				str_comments.append(comments_json['data'][y]['message'].encode('utf-8'))

	if posts_json['paging'] != "" and posts_json['paging']['next'] != "":
		posts_next_page = posts_json['paging']['next']
		posts_next_page = base_url + posts_next_page[32:]
	else:
		posts_next_page = ""

#feed
feeds_next_page = base_url + gojek_id + "/feed?limit=100&access_token="+token
feeds = requests.get(feeds_next_page)
feeds_json = feeds.json()

for x in range(0, len(feeds_json['data'])):
	print "feeds " + str(x)
	if feeds_json['data'][x].has_key('message'):
		str_comments.append(feeds_json['data'][x]['message'].encode('utf-8'))


# Write to CSV
f = open("test_fb.csv", "wb+")
writer = csv.writer(f)
for item in str_comments:
    writer.writerow([item])