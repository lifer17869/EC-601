from unittest import TestCase
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import string

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
def percentage(part,whole):
    return 100 * float(part)/float(whole) 


def result():
	positive  = 0
	negative = 0
	neutral = 0
	polarity = 0
	tweet_list = []
	neutral_list = []
	negative_list = []
	positive_list = []
	tweets =["I hate this film"]
	noOfTweet = int(len(tweets))
	for tweet in tweets:
	    
	    #print(tweet.text)
	    tweet_list.append(tweet)
	    analysis = TextBlob(tweet)
	    score = SentimentIntensityAnalyzer().polarity_scores(tweet)
	    neg = score['neg']
	    neu = score['neu']
	    pos = score['pos']
	    comp = score['compound']
	    polarity += analysis.sentiment.polarity
	    
	    if neg > pos:
	        negative_list.append(tweet)
	        negative += 1

	    elif pos > neg:
	        positive_list.append(tweet)
	        positive += 1
	    
	    elif pos == neg:
	        neutral_list.append(tweet)
	        neutral += 1

	positive = percentage(positive, noOfTweet)
	negative = percentage(negative, noOfTweet)
	neutral = percentage(neutral, noOfTweet)
	polarity = percentage(polarity, noOfTweet)
	positive = format(positive, '.1f')
	negative = format(negative, '.1f')
	neutral = format(neutral, '.1f')
	noOfTweet = int(len(tweets))
	tweet_list = pd.DataFrame(tweet_list)
	neutral_list = pd.DataFrame(neutral_list)
	negative_list = pd.DataFrame(negative_list)
	positive_list = pd.DataFrame(positive_list)
	print("total number: ",len(tweet_list))
	print("positive number: ",len(positive_list))
	print("negative number: ", len(negative_list))
	print("neutral number: ",len(neutral_list))
	return True
class TryTesting(TestCase):
    def test_always_passes(self):
    	assert result() == True
    	self.assertTrue(True)