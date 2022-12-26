import os

import tweepy
from dotenv import load_dotenv

load_dotenv()


client = tweepy.Client(
    consumer_key=os.getenv("consumer_key"),
    consumer_secret=os.getenv("consumer_secret"),
    access_token=os.getenv("access_token"),
    access_token_secret=os.getenv("access_token_secret"),
)

print(client.get_home_timeline())

# Create API object with proxy
# api = tweepy.API(auth)
# api.verify_credentials()
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")
