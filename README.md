# Twitter actions bot built with Python3 and Tweepy
An simple and easy to run Python3 twitter bot. It can search keywords, like, retweet and reply to tweets. Full configurable.

## How to
----------

This bot is built using [Tweepy](http://www.tweepy.org/), an library in python that encapsulates the work of using Twitter's api.

To install the dependencies you can run:

`pip install tweepy`

Or:

`pip install requirements.txt`

* Before running a twitter bot, please read the [Twitter's rules](https://support.twitter.com/articles/76915). Please ***do not spam***. 

Instructions
----------
The first thing you will need to do is to create a twitter application and get your credentials, you will need the consumer, access and bearer tokens. 

* Create a new [Twitter Application](https://apps.twitter.com/app/new). 

After that, configure the bot using the env vars exported on the file run.sh. Please replace all the ****** with your personal tokens.

You can also tweak with the configurations:
- Changing the **GREETING_MESSAGE** will change the message used on replies
- Changing the **KEYWORDS_LIST** will change what keywords the bot will search
- Changing the **MAX_RESULTS** will change the max number of results that your bot will interact with each key defined in KEYWORDS_LIST.
- Changing **TIME_LIMIT_HOURS** will change how back in time the bot will search the keywords
- **RETWEET**, **LIKE** and **REPLY** must be set to "on" if you want the bot to perform the actions, and to "off" if not.

Then, to execute the bot please run:

`make run`

Bonus: automatically run the bot 
----------
* Create a [Cron Job](https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800) or use [Task Scheduler](https://technet.microsoft.com/en-us/library/cc748993(v=ws.11).aspx) to automate this script.
* This bot can be easily used with [Heroku](https://www.heroku.com) and the add-on [Heroku Scheduler](https://www.youtube.com/watch?v=QeTGN47WtOE) to run alone in the cloud.
