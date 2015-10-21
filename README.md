# Tweets Monitor
This tiny app written in Python uses [Tweepy](https://github.com/tweepy/tweepy/) library and allows to retrieve in real time (via Twitter's streaming API) those tweets tagged with some predefined _hashtags_ 

In order to use the script, it's needed to install Tweepy in your Python environment (or in a _virtualenv_)

    pip install tweepy

Also, you need to configurate the parameters _consumer_key_, _consumer_secret_, _access_token_, _access_token_secret_ and those  _hashtags_ that will be monitorized. When running the script, redirect the script's output to a file (TXT for example) that will save the retrieved tweets:

    python tuits-monitor.py > filename.txt


Note: In future versions, this  _crawler_ will use a database in order to keep the retrieved tweets. At the moment, keep patience :) 
