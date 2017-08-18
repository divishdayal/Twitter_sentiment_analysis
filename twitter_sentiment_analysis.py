import tweepy
import sys
from textblob import TextBlob

consumer_key = 'xlA6WajQzoByEiogAmePKUGNa'
consumer_secret = 'AeeCL4514VRar7Xj4XXf1mveKQc5rxjp6jntHWUfaICS6zQ2Pp'

access_token = '3252674191-7JlVINPJv6fe5Y76KZvQO4wfLccs8gEeEzaOlkl'
access_token_secret = 'yTMC0NhqWO9s0mJr21vBsUW8nSkb9XyQYxa7r2VdEVKJX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets_retrieved = api.search(sys.argv[1])

total = 0
count = 0

for tweet in tweets_retrieved:
	analysis = TextBlob(tweet.text)
	total += analysis.sentiment.polarity
	count += 1

print total/count