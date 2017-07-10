import re
import csv
import json

#filename = "result6.json"
filename = "result.json"
with open(filename, 'r') as content_file:
    content = content_file.read()

#content = content.encode('ascii', 'ignore').decode('ascii')

x = json.loads(content)

f = csv.writer(open("tweets.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
#f.writerow(["text"])
'''
for x in x:
f.writerow([x["text"]])
'''

f = open("test1.csv", "wb+")
print "write to csv"
writer = csv.writer(f)


for item in x:
	text = re.sub(r"http(.)*?(\s|$)", "", item['text'])
	text = re.sub(r"\s*", " ", text)
    writer.writerow([])