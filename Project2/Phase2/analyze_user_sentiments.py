import tweepy
from google.oauth2 import service_account
from google.cloud import language_v1
import configparser
import csv
from google.cloud.language_v1 import types
import pandas as pd
import sys

#read config




def getTwitterMess(api):
    user = input('Enter the user you want to analyze:')
    limit = 30
    tweetsUsers = tweepy.Cursor(api.user_timeline, screen_name = user, count = 30, tweet_mode = 'extended').items(limit)
    data = []
    for tweetUser in tweetsUsers:
        data.append([tweetUser.user.screen_name, tweetUser.full_text])

    df1 = pd.DataFrame(data)
    df1.to_csv('tweetsUserOutput.csv')



def analyze_sentiment():
    client = language_v1.LanguageServiceClient(credentials=credentials)
    filOpen = open('tweetsUserOutput.csv',mode = 'r',encoding = 'utf-8')
    data = csv.reader(filOpen,delimiter=',')
    texts = []
    sentiments = []
    for row in data:
        texts.append(row[2])

    for t in texts:
        document = types.Document(
        content = t,
        type = language_v1.Document.Type.PLAIN_TEXT)

        sentiment = client.analyze_sentiment(
            request={"document":document}
        ).document_sentiment

        sentiments.append(sentiment)
    for j in range(len(texts)):
        print("Text: {}".format(texts[j]))
        print("Sentiment: {}, {}".format(sentiments[j].score, sentiments[j].magnitude))



if __name__=="__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_key = config['Twitter']['api_key']
    api_key_secret = config['Twitter']['api_key_secret']
    access_token = config['Twitter']['access_token']
    access_token_secret = config['Twitter']['access_token_secret']
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    getTwitterMess(api)
    credentials = service_account.Credentials.from_service_account_file("C:/Users/cxysz/Downloads/ec601phase2-5034049bb0eb.json")
    analyze_sentiment()