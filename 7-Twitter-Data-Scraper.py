import json
import tweepy
import nltk
import re
import operator
import string
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

# Section defining some emojis/regex stuff
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

punc = list(string.punctuation)
stop = stopwords.words('english') + punc + ['rt', 'via']

# Proc a single status
for status in tweepy.Cursro(api.home_timeline).items(10):
    process_or_store(status._json)

# List of all followers
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

# List of all our tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

# This gathers all new tweets with the defined hashtag
class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json','a') as i:
                i.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    
    def on_error(self, status):
        print(status)
        return True
    
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#animenews'])

fname = 'status.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Below grabs all terms not in stopwords and punc and common phrases like rt and via
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        count_all.update(terms_stop) # Updates counter
    print(count_all.most_common(5)) # Prints the defined number of most common terms
