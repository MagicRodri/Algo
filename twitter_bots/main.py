import os

import tweepy
from dotenv import load_dotenv

load_dotenv()
# Authenticate to Twitter
API_KEY = os.getenv("consumer_key")
API_SECRET = os.getenv("consumer_secret")
auth = tweepy.OAuth1UserHandler(API_KEY,API_SECRET)
auth.set_access_token(os.getenv("access_token"),os.getenv("access_token_secret"))

# Create API object with proxy
api = tweepy.API(auth, proxy="")
api.verify_credentials()
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")
