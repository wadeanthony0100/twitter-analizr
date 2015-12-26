import nltk
import tweepy
import time
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# My app's constants
API_KEY = 'X'
API_SECRET = 'X'

ACCESS_TOKEN = 'X'
ACCESS_TOKEN_SECRET = 'X'

# stop words include the typical set, plus some common Twitter tokens
stop_words = set(nltk.corpus.stopwords.words('english')) | set(['@', '#', 'RT', 'http', 'https'])

lemmatizer = nltk.stem.WordNetLemmatizer()

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tokens = nltk.word_tokenize(status.text)
        tokens = set(tokens) - stop_words
        lemmatized_tokens = set()
        for token in tokens:
            lemmatized_tokens.add(lemmatizer.lemmatize(token))
        #print(tokens, ' -> ', lemmatized_tokens)
        

def authenticate():
    # Authenticate with the Twitter system
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    ##redirect_url = auth.get_authorization_url()
    # Ask the user to visit a url
    ##print('Please visit this address, allow this app, and copy the key', redirect_url)
    ##pin = input('Twitter auth pin: ')
    # Get access token
    #auth.get_access_token(pin)
    # Construct the API instance
    api = tweepy.API(auth)
    return api

@app.route('/')
def hello():
        return render_template('index.html')

@app.route('/get_tweet')
def getTweet():
    return jsonify(user='wad', tweet='Im tweeting yay', loc='US')

def startServer():
    api = authenticate()
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.sample(languages=['en'],  async=True)
    app.run()
    while true:
        time.sleep(5)
        getTweet()

startServer()
