import urllib3, facebook, requests, json, csv, sys, MySQLdb

# You might have to update the token
token= '_YOUR_ACCESS_TOKEN_'
gojek_id = "166677693366218"
base_url = "https://graph.facebook.com/v2.7/"
graph = facebook.GraphAPI(access_token=token, version = 2.7)
filename = "facebook.csv"

f = open(filename, "wb+")
writer = csv.writer(f)


comment_message = []
posts_next_page = base_url + gojek_id + "/posts?limit=100&access_token="+token

k = 0
while posts_next_page != "" and k != 10:
	posts = requests.get(posts_next_page) 
	posts_json = posts.json()
	print "posts"

    # Get post id
	for x in range(0, len(posts_json['data'])):
		post_id = posts_json['data'][x]['id']

		comments_next_page = base_url + post_id + "/comments?limit=100&access_token="+token
		while comments_next_page != "":
			comments = requests.get(comments_next_page)
			comments_json = comments.json()

			print "comments " + str(x)
			if comments_json.has_key('data'):
				print "Total comment: " + str(len(comments_json['data']))

				for y in range(0, len(comments_json['data'])):
					data = [ \
						comments_json['data'][y]['message'].encode('utf-8'),
						comments_json['data'][y]['created_time'].encode('utf-8'),
						comments_json['data'][y]['id'].encode('utf-8')]
					comment_message.append(data)
					writer.writerow(item)

				if comments_json.has_key('paging') and comments_json['paging'].has_key('next'):
					comments_next_page = comments_json['paging']['next']
					comments_next_page = base_url + comments_next_page[32:]
				else:
					comments_next_page = ""
	if posts_json['paging'] != "" and posts_json['paging']['next'] != "":
		posts_next_page = posts_json['paging']['next']
		posts_next_page = base_url + posts_next_page[32:]
	else:
		posts_next_page = ""
	k += 1

# Get comment from facebook feed
feeds_next_page = base_url + gojek_id + "/feed?limit=100&access_token="+token
while feeds_next_page != "":
	feeds = requests.get(feeds_next_page)
	feeds_json = feeds.json()

	for x in range(0, len(feeds_json['data'])):

		print "feeds " + str(x)
		if feeds_json['data'][x].has_key('message'):
			data = [ \
				feeds_json['data'][x]['message'].encode('utf-8'), \
				feeds_json['data'][x]['created_time'].encode('utf-8'), \
				feeds_json['data'][x]['id'].encode('utf-8')]
			comment_message.append(data)
			writer.writerow(item)

	if feeds_json.has_key('paging') and feeds_json['paging'].has_key('next'):
		feeds_next_page = feeds_json['paging']['next']
		feeds_next_page = base_url + feeds_next_page[32:]
	else:
		feeds_next_page = ""
