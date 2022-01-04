def get(keys, client, max_results, start_time, blocked_ids):
    public_tweets = []
    for key in keys:
        unparsed_tweet = client.search_recent_tweets(key, max_results=max_results, start_time=start_time, expansions = ['author_id'])
        if(unparsed_tweet[0] != None):
            public_tweets += unparsed_tweet[0]
    for public_tweet in public_tweets:
        if public_tweet.author_id in blocked_ids or public_tweet.data['text'].startswith('RT'):
            public_tweets.remove(public_tweet)
    return public_tweets


def like(client, id, should_like):
    if not should_like:
        return
    try:
        client.like(id)
        print(f'Liked {id}')
    except:
        print(f'Like on tweet {id} ignored')


def retweet(client, id, should_retweet):
    if not should_retweet:
        return
    try:
        client.retweet(id)
        print(f'Retweeted {id}')
    except:
        print(f'Retweet on tweet {id} ignored')


def reply(client, id, message, should_reply):
    if not should_reply:
        return
    try:
        client.create_tweet(text=message, in_reply_to_tweet_id=id)
        print(f'Replied {id}')
    except:
        print(f'Reply on tweet {id} ignored')


def blocked(client):
    blocked_ids = []
    try:
        unparsed_blockeds = client.get_blocked()
        for blocked_user in unparsed_blockeds[0]:
            blocked_ids.append(blocked_user.id)
    except:
        print('An error occurred while getting blocked users')
    return blocked_ids