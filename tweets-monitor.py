#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after

consumer_key="myConsumerKey"
consumer_secret="myConsumerSecret"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section

access_token="myAccessToken"
access_token_secret="myAccessTokenSecret"

# Define your hashtags list to be monitorized
hashtags_list = ['#Hashtag1', '#Hashtag2', '#Hashtag3']

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream.
	This is a basic listener that just prints received tweets to stdout.
	"""
	def on_data(self, data):
		try:
			print(data)
			return True
		except:
			pass
		
	#def on_status(self, status):
	#	print(status.text)

	def on_error(self, status):
		print(status)
	
	def on_timeout(self):
		sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
		time.sleep(60)
		return 

if __name__ == '__main__':
	
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(track=hashtags_list)
