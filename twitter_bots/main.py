import logging

import config
import db
import twitter
from bot import MarketCapBot

if config.DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

def main():

    logging.info("Starting bot...")
    bot = MarketCapBot(db.ohlcv_db,db.posts_db,twitter.client)
    pair_to_post = bot.get_pair_to_post()
    message = bot.compose_message(pair=pair_to_post)
    bot.post_message(pair=pair_to_post,message=message)

if __name__ == "__main__":
    main()
