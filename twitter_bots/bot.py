import logging

import pymongo

import db
import twitter


class MarketCapBot:
    """ 
        Class to represent the MarketCapBot
    """

    def __init__(
        self,
        ohlcv_db:pymongo.collection.Collection,
        posts_db:pymongo.collection.Collection,
        twitter_client
        ):

        """
            Constructor for MarketCapBot
        """
        logging.info("Initializing MarketCapBot...")
        self.ohlcv_db = ohlcv_db
        self.posts_db = posts_db
        self.twitter_client = twitter_client
    
    def _get_pair_to_post(self)-> str:
        """
            Method to return the pair to post
        """
        top_pairs = db.get_top_pairs(max_num=100)
        oldest_posted_pairs = db.get_oldest_posted_pairs(top_pairs,max_num=5)
        pair_to_post = db.get_pair_to_post(top_pairs,oldest_posted_pairs)
        return pair_to_post
        

    def _get_message_dict(self,pair:str=None,pair_symbol:str=None,pair_base:str=None) -> dict:
        """
            Method to return a dictionary of marketVenue:volume percentage for a given pair
        """
        if pair is None and (pair_symbol is None or pair_base is None):
            raise ValueError("Either pair or pair_symbol and pair_base must be provided")
        elif pair is None:
            pair = self._get_pair_to_post()
        elif pair is not None:
            try:
                pair_symbol = pair.split('-')[0].lower()
                pair_base = pair.split('-')[1].lower()
            except:
                raise ValueError("Invalid pair provided, must be in the format 'SYMBOL-BASE")
                
        ohlcv_documents_for_pair = self.ohlcv_db.find({'pair_symbol':pair_symbol,'pair_base':pair_base}).sort([
            ('timestamp', pymongo.DESCENDING),
            ])

        latest_date = None
        message_dict = {
            'others':0
        }
        for item in ohlcv_documents_for_pair:
            
            if latest_date is None:
                latest_date = item['timestamp']
            if item['timestamp'] == latest_date:
                # pprint.pprint(item)
                if item['marketVenue'] not in message_dict:
                    if len(message_dict) <= 5:
                        # key for top 5 marketVenues
                        message_dict[item['marketVenue']] = float(item['volume'])
                    else:
                        # store the rest in 'others'
                        message_dict['others'] += float(item['volume'])
                    continue    
                message_dict[item['marketVenue']] += float(item['volume'])
            else:
                break
        total_volume = sum(message_dict.values())
        message_dict = {key:round((value/total_volume)*100,2) for key,value in message_dict.items()}
        return message_dict

    def compose_message(self,pair:str=None,message_dict:dict=None) -> str:
        """
            Function to compose a message for a given pair and message_dict
        """

        if pair is None:
            pair = self._get_pair_to_post()
        if message_dict is None:
            try:
                message_dict = self._get_message_dict(pair=pair)
            except Exception as e:
                logging.debug('Error getting message_dict',e)
        
        logging.info("Composing message...")  
        message = f"Top 5 marketVenues for {pair}:\n"
        for marketVenue,percentage in sorted(message_dict.items()):
            message += f"{marketVenue.capitalize()}: {percentage}%\n"
        return message


if __name__ == "__main__":
    bot = MarketCapBot(db.ohlcv_db,db.posts_db,twitter.client)
    print(bot.compose_message())