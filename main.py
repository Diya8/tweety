import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from bs4 import BeautifulSoup as SOUP
import requests as HTTP
import config


def get_movie(emotion):
	'''
	Function to web scrape from IMDb website by genre depending on user mood
	'''
	if(emotion == "neutral"):
		urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "negative"):
		urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "positive"):
		urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

	response = HTTP.get(urlhere)
	data = response.text

	soup = SOUP(data, "lxml")

	title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
	return title

def clean_tweet(tweet):
	'''
	Function to clean tweet text
	'''

	tweet = ' '.join(re.sub("('RT')|(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
	if tweet[:2] == "RT":
		tweet = tweet[3:]
	return tweet

class TwitterClient(object):
	'''
	Generic Twitter Class
	'''
	
	def __init__(self):
		'''
		Constructor for authentication
		'''

		try:
			self.auth = OAuthHandler(config.consumer_key, config.consumer_secret)
			self.auth.set_access_token(config.access_token, config.access_token_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def get_tweet_sentiment(self, tweet):
		'''
		Function for analysing tweet sentiment
		'''

		analysis = TextBlob(tweet)
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def get_tweets(self, count):
		'''
		Function to fetch tweets
		'''

		tweets = []

		try:
			fetched_tweets = self.api.user_timeline(count=count)
			for i in range(len(fetched_tweets)):
				fetched_tweets[i].text = clean_tweet(fetched_tweets[i].text)
			for tweet in fetched_tweets:
				parsed_tweet = {}
				parsed_tweet['text'] = tweet.text
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
				if tweet.retweet_count > 0:
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			return tweets

		except tweepy.TweepError as e:
			print("Error : " + str(e))

def main():

	# Object of TwitterClient class is created
	api = TwitterClient()

	# Calling get_tweets method
	tweets = api.get_tweets( count = 100)

	# Tweets classified and stored and sentiment percentage is calculated

	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	pos = 100*len(ptweets)/len(tweets)
	
	print("Positive tweets percentage: {:.2f} %".format(pos))

	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	neg = 100*len(ntweets)/len(tweets)

	print("Negative tweets percentage: {:.2f} %".format(neg))

	neut = 100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets)
	print("Neutral tweets percentage: {:.2f} % ".format(neut))

	# Emotion the user feels the most is calculated
	d = {'positive': pos, 'negative': neg, "neutral": neut}
	emotion = max(d, key=d.get)

	print("\nYou've been feeling", emotion, "recently. We've got just the right recommendations for you to watch!\n")

	# Recommendations gathered and listed
	a = get_movie(emotion)
	count = 0

	for i in a:
		tmp = str(i).split('>')

		if(len(tmp) == 3):
			print(tmp[1][:-3])

		if(count > 11):
			break
		count+=1


if __name__ == "__main__":

	main()
