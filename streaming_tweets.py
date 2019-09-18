# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:02:18 2019

@author: Vinayak
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
import print_tweets

 
import twitter_credentials
 

class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list,max_tweets,user):
        listener = StdOutListener(fetched_tweets_filename,max_tweets,user)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)



class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename,max_tweets,user):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.max_tweets=max_tweets
        self.user=user

    def on_data(self, data):
        
        global tweets_list
        tweets_list.append(data)
        print(len(tweets_list))
        #print(data)
        if (len(tweets_list)==self.max_tweets):
            print_tweets.print_tweets(tweets_list,self.user)
            #break

          

    def on_error(self, status):
        print(status)

 

def main(user):
    hash_tag_list = input('Enter HashTag to search for the tweets')
    max_tweets= int(input('Enter number of max tweets to diplay'))
    fetched_tweets_filename = "tweets.txt"
    
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list,max_tweets,user)
