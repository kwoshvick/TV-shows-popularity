import tweepy
import csv
from twitter.credentials import Credentials


c = Credentials()

api = c.authentinticate_twitter()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print (tweet.text)




with open('../bahati.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["text"])
    for tweet in tweepy.Cursor(api.search, q="#BeingBahati", count=1000,
                               lang="en",
                               since="2016-04-03").items():


        writer.writerow([tweet.text,])
# pass
    # print (tweet.text)
    # print("-----------")
