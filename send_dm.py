import tweepy
import config
import re
import webbrowser

def negative_emote_trigger():
	'''
	Function is called when user has been experiencing prolonged negative emotions
	'''

	auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)

	api = tweepy.API(auth)
	me = api.me()

	# A direct message is sent to the user's chosen contact
	friend = api.get_user(USER_ID)
	api.send_direct_message(friend.id, "Hey, your friend @" + me.screen_name + " has been feeling a bit down lately. Would you like to check up on them?\n\nMessage from TweepyApp")

	# A Twitter resource on Mental Health is opened on the default web browser
	webbrowser.open("https://twitter.com/DBSAlliance")
