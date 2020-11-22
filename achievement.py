import tweepy
import config
import re
from datetime import datetime

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

month = datetime.now().strftime('%B')
challenge_name = "WakeUpBefore5_30"

challenge_status = input("Have you completed this month's challenge?")

# If the challenge has been completed, a message is tweeted out with the month and challenge name
if challenge_status.lower() == "yes":
	api.update_status("Feeling great! Just finished a Tweety challenge! #Tweety" + month + "Challenge" + "  #" + challenge_name +" 😍😊❤🙌") 