import tweepy
from datetime import *
from keys import *
from api import *


def main():
    start_time = datetime.today() + timedelta(hours=-time_limit_hours)
    client = tweepy.Client(bearer, consumer_key, consumer_secret, access_token, access_token_secret)
    blocked_ids = blocked(client)
    tweets = get(keywords_list, client, max_results, start_time, blocked_ids)

    for tweet in tweets:
        like(client, tweet.id, should_like)
        retweet(client, tweet.id, should_retweet)
        reply(client, tweet.id, greeting_message, should_reply)

    print(f'Processed {len(tweets)} tweets')

if __name__ == "__main__":
    main()
