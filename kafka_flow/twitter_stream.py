from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient, KafkaProducer
import json
from credentials import CredentialsManager

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send('LogicalStructure2', data.encode('utf-8'))
        print(data)
        return True
    def on_error(self, status):
        print (status)

producer = KafkaProducer(bootstrap_servers='192.168.43.138:9092', api_version=(0,10))
l = StdOutListener()
credentials = CredentialsManager('credentials.txt')
access_token, access_token_secret, consumer_key, consumer_secret = credentials.parse()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="trump")
