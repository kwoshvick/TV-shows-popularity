import tweepy
from twitter.credentials import Credentials


c = Credentials()

api = c.authentinticate_twitter()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print (tweet.text)


for tweet in tweepy.Cursor(api.search,q="#nairobidiaries",count=100,
                           lang="en",
                           since="2016-04-03").items():
    print (tweet.created_at, tweet.text)
