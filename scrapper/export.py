import csv
import json

#filename = "result6.json"
filename = "comment.json"
with open(filename, 'r') as content_file:
    content = content_file.read()

#content = content.encode('ascii', 'ignore').decode('ascii')

x = json.loads(content)

f = csv.writer(open("tweets.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["text", "tweet_id", "user_id", "favorite_count", "created_at"])

for x in x:
    f.writerow([x["text"],
                x["user"]["id"],
                x["id"],
                x["favorite_count"],
                x["created_at"]])