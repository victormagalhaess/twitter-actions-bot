import os
import json

max_results = int(os.getenv('MAX_RESULTS'))
time_limit_hours = int(os.getenv('TIME_LIMIT_HOURS'))
keywords_list = json.loads(os.environ['KEYWORDS_LIST'])
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer = os.getenv('BEARER')
greeting_message = os.getenv('GREETING_MESSAGE')
