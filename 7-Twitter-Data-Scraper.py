import tweepy
import pandas as pd
import operator
import json
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

consumer_key = 'dB4VBVnnepK2ZqU2qc0XyHGLj'
consumer_secret = 'VmEw22eqJwdJBGjeES7nWwcvDXiSuDNiW3HHlWr0PNya2BkCVP'
access_token = '1599636079539257345-4lMwNnKZLNv4cehjq3AWsFRDiMiK6G'
access_secret = 'mmlkJ8yui3PU5FS0OUi3J7CDuZyDad6QkyDzBMtY56SPI'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAIzt3wEAAAAAoLHf0RsEJvHJlQ3OVx9xDF6SQw4%3DFc8WoHFO7dsslpK8nnqTmGyzm6otoK4YwnZyqwJ3dFXC4ry4P5'
 
auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token)

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']


# Funcs and Classes
def process_or_store(tweet):
    print(json.dumps(tweet))

# Tokenize the tweet
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

with open('mytweets.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])

# Active Code
for status in tweepy.Cursor(api.home_timeline).items(1):
    process_or_store(status._json)
# Change the api.x to whichever. E.g. friends, user_timeline, etc.
# The number in the items param dets the number of tweets to scrape

response = client.search_recent_tweets("python")
# This searches recent (7 days) tweets for said term, default max 10
# Use response = client.search_recent_tweets("Tweepy", max_results=100) e.g. to define a max num
# Use client.search_all_tweets instead for non recent
tweets = response.data
with open("tweets.json", "w", encoding="utf-8") as f:
    json.dump(tweets, f, ensure_ascii=False, indent=4) # Indent is pretty print

fname = 'tweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # List all the terms out without hastags or mentions
        terms_only = [term for term in preprocess(tweet['text']) 
              if term not in stop and
              not term.startswith(('#', '@'))] 
        # Update counter
        count_all.update(terms_all)
    print(count_all.most_common(5)) # Print top 5 most common
