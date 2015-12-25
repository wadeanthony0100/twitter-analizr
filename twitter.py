import nltk
import tweepy
import json

# My app's constants
CONSUMER_TOKEN = 'XXXXX'
CONSUMER_SECRET = 'XXXXX'
API_KEY = 'XXXXX'
API_SECRET = 'XXXXX'
OWNER_ID = 'XXXXX'
AUTH_REQ = 'XXXXX'

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

def authenticate():

    # Authenticate with the Twitter system
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    redirect_url = auth.get_authorization_url()

    # Ask the user to visit a url
    print('Please visit this address, allow this app, and copy the key', redirect_url)
    pin = input('Twitter auth pin: ')

    # Get access token
    auth.get_access_token(pin)

    # Construct the API instance
    api = tweepy.API(auth)
    return api

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
