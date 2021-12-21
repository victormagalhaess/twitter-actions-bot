import tweepy
from datetime import *
from keys import *
from api import *


def main():
    start_time = datetime.today() + timedelta(hours=-time_limit_hours)
    client = tweepy.Client(bearer, consumer_key, consumer_secret, access_token, access_token_secret)
    tweets = get(keywords_list, client, max_results, start_time)

    for tweet in tweets:
        like(client, tweet.id)
        retweet(client, tweet.id)
        reply(client, tweet.id, greeting_message)

    print(f'Processed {len(tweets)} tweets')

if __name__ == "__main__":
    main()
