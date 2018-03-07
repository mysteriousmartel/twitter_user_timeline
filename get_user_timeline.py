#!/usr/bin/env python

import tweepy
from datetime import datetime

#get your own keys from apps.twitter.com
ckey = 'ckey'
csecret = 'csecret'
atoken = 'atoken'
asecret = 'asecret'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

jarvis = 'AlistairJarvis'
uuk = 'UniversitiesUK'

def getTimeLineFor(name):
	results = api.user_timeline(screen_name = name, count = 100, include_rts = True)

	file_contents = ""

	for status in results:
		print status.text
		print "\n"
		file_contents+=status.text
		file_contents+="\n"
		print status.created_at
		print "\n"
		file_contents+=status.created_at.strftime("%a %b %d %H:%M:%S +0000 %Y")
		file_contents+="\n"
		print status.source
		print "\n"
		file_contents+=status.source
		file_contents+="\n"
		file_contents+="\n"



	text_file = open(name+"_tweets.txt", "w")
	text_file.write(file_contents.encode('utf-8'))
	text_file.close()


if __name__ == "__main__":
	getTimeLineFor(jarvis)
	getTimeLineFor(uuk)