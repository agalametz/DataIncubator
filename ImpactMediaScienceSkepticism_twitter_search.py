import csv
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
 
consumer_key = 'nROnzajpiF03wrDEAHpkERFSJ'
consumer_secret = 'QkbQqfY6Ps15psBK8YvER7SCzQ6m8WV4NQ8CMmtn68vx6FgjBV'
access_token = '862790517024849920-KqtFSSKJMElbbHeSNxM8i21bVzqLcKb'
access_secret = 'j6pDq65mKS4rFxGawmusyQHIE0AOt8CYVOyY7sP967XMG'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#Exemple of current streaming of tweets - here for the keyword 'CNN' 
# Streaming of tweets with keyword = '#CNN'
#class MyListener(StreamListener): 
#    def on_data(self, data):
#        try:
#            with open('cnn.json', 'a') as f:
#                f.write(data)
#                return True
#        except BaseException as e:
#            print("Error on_data: %s" % str(e))
#        return True 
#    def on_error(self, status):
#        print(status)
#        return True 
#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#CNN'])

def retrieve(search_terms,namefile):
    tw = tweepy.Cursor(api.search, q=search_terms).items()#10000)
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tw]
    with open(namefile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

search_terms = '%23CNN AND "climate change"'
retrieve(search_terms,'CNN_climatechange.json')
search_terms = '%23BBC AND "climate change"'
retrieve(search_terms,'BBC_climatechange.json')
search_terms = '%23FoxNews AND "climate change"'
retrieve(search_terms,'FoxNews_climatechange.json')
search_terms = 'LastWeekTonight AND "climate change"'
retrieve(search_terms,'LastWeekTonight_climatechange.json')
search_terms = '%23CNBC AND "climate change"'
retrieve(search_terms,'CNBC_climatechange.json')
search_terms = '%23MSNBC AND "climate change"' 
retrieve(search_terms,'MSNBC_climatechange.json')
search_terms = '%23CNN AND vaccines' 
retrieve(search_terms,'CNN_vaccines.json')
search_terms = '%23BBC AND vaccines'
retrieve(search_terms,'BBC_vaccines.json')
search_terms = '%23FoxNews AND vaccines'
retrieve(search_terms,'FoxNews_vaccines.json')
search_terms = 'LastWeekTonight AND vaccines'
retrieve(search_terms,'LastWeekTonight_vaccines.json')
search_terms = '%23CNBC AND vaccines'
retrieve(search_terms,'CNBC_climatechange.json')
search_terms = '%23MSNBC AND vaccines'
retrieve(search_terms,'MSNBC_climatechange.json')
search_terms = '%23CNN AND science'
retrieve(search_terms,'CNN_science.json')
search_terms = '%23BBC AND science'
retrieve(search_terms,'BBC_science.json')
search_terms = '%23FoxNews AND science'
retrieve(search_terms,'FoxNews_science.json')
search_terms = 'LastWeekTonight AND science'
retrieve(search_terms,'LastWeekTonight_science.json')
search_terms = '%23CNBC AND science'
retrieve(search_terms,'CNBC_science.json')
search_terms = '%23MSNBC AND science'
retrieve(search_terms,'MSNBC_science.json')

