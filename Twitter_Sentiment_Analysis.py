import tweepy
from textblob import TextBlob

consumer_key = 'T8EO3pT8MrnLlIt41Y7rhODsK'
consumer_secret = 'PblUA3oXfy7kfIxVbnZhOnq6ADHsespvlhmY8irfUIjNR0Czmr'


access_token = '28435179-l0sMMPFpTYYjR861MEX4MHOMdkaV9LUnZD5TMrI7z'
access_token_secret = 'K8bXzaKPFXwLEz8e0YcGAZ03G5KZwXuauYoqbdH3DorHJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Annoying_girlfriend')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)