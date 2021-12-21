def get(keys, client, max_results, start_time):
    public_tweets = []
    for key in keys:
        unparsed_tweet = client.search_recent_tweets(key, max_results=max_results, start_time=start_time)
        if(unparsed_tweet[0] != None):
            public_tweets += unparsed_tweet[0]
    return public_tweets


def like(client, id):
    try:
        client.like(id)
        print(f'Liked {id}')
    except:
        print(f'Like on tweet {id} ignored')


def retweet(client, id):
    try:
        client.retweet(id)
        print(f'Retweeted {id}')
    except:
        print(f'Retweet on tweet {id} ignored')


def reply(client, id, message):
    try:
        client.create_tweet(text=message, in_reply_to_tweet_id=id)
        print(f'Replied {id}')
    except:
        print(f'Reply on tweet {id} ignored')
