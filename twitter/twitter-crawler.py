import os
import csv
import tweepy
import datetime
from twitter.credentials import Credentials
from twitter.cleaner import Cleaner



credentials = Credentials()
cleaner = Cleaner()
api = credentials.authentinticate_twitter()

today = datetime.date.today()
path = "../dataset/crawled/"+str(today)
# os.mkdir(path)

hashtags =[
    # 'BeingBahati'
    # 'AuntieBoss',
    # 'theTrend',
    # 'HeyAmina',
    'WickedEdition'
    'Mafundi',
    'PressPass',
    'LivingWithEss',
    'NTVWild',
    'InHouse',
    'LIT360',
    'TopSport',
    'NTVPropertyShow',
    'ChurchillShow',
    'ChurchillRaw',
    'Crossover101',
    'NTVJamrock',
    'TeenRepublik',
    'PasswordPlus',
    'AMLiveNTV',
    'PapaShirandula',
    'TahidiHigh',
    'KLive',
    'OneLove',
    'Machachari',
    'setoEastAfrica',
    'Bambika',
    'MySweetCurse',
    'WomanWithoutLimits',
    'InspektaMwala',
    'ShambaShapeUp',
    '10over10',
    'TheGirlNamedFeriha',
    'FallIntoTemptation',
    'Afrosinema',
    'MorningExpress',
    'TheEntrepreneur',
    'MaishaMzuqa',
    'TheSwitch',
    'K24Alfajiri',
    'TalkCentral',
    'K24Tizi',
    'NMGLeadershipForum',
    'CaseFiles',
    'TheChamwadaReport',
    'tnlwithdrofweneke',
    'Tukuza',
    'NewViojaMahakamani',
    'Vitimbi',
    'ChiniYaMnazi',
    'Daktari',
    'AfricaLD',
    'Tujaribu',
    'DaringAbroad'
]



for hashtag in hashtags:
    with open(path+'/' + hashtag + '.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["text", "label"])
        for tweet in tweepy.Cursor(api.search, q="#"+hashtag,).items():
            writer.writerow([cleaner.clean_tweets(tweet.text),])

