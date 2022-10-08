import tweepy
import configparser
import pandas as pd

#read config
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['Twitter']['api_key']
api_key_secret = config['Twitter']['api_key_secret']
access_token = config['Twitter']['access_token']
access_token_secret = config['Twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
# find public tweets 
public_tweets = api.home_timeline()

col = ['Time', 'User', 'Tweet']

data = []
for tweetpub in public_tweets:
    data.append([tweetpub.create_at, tweetpub.user.screen_name, tweetpub.text])

# get output into a csv file
df = pd.DataFrame(data, columns = col)
df.to_csv('tweetsOutput.csv')
# 
# 
# 
# find a specific user tweet 
user = 'veritasium'
limit = 30

tweetsUsers = tweepy.Cursor(api.user_timeline, screen_name = user, count = 30, tweet_mode = 'extended').items(limit)
columns = ['User', 'Tweet']
data1 = []

for tweetUser in tweetsUsers:
    data1.append([tweetUser.user.screen_name, tweetUser.full_text])

df1 = pd.DataFrame(data1, columns = columns)
df1.to_csv('tweetsUserOutput.csv')
# 
# 
# 
# search specific keywords
keywords = '#2022'
tweetsHash = tweepy.Cursor(api.search_tweets, q = keywords, count = 30, tweet_mode = 'extended').items(limit)
data2 = []

for hashtage in tweetsHash:
    data2.append([hashtage.user.screen_name, hashtage.full_text])

df2 = pd.DataFrame(data2, columns = columns)
df2.to_csv('tweetsHashTagOutput.csv')