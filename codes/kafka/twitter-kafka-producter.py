#!/usr/bin/env python

from kafka import SimpleProducer, KafkaClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
topic = "sri"
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages(topic, data.encode('utf-8'))
        return True

    def on_error(self, status):
        print(status)

listener_producer = StdOutListener()
auth = OAuthHandler("kH84uQAU3Wjtgks6OLKXIdBil", "rjZBI1x2Tv7XbDEBGbZRZrskWwGc9Afqqb20YGD7NXHsVw9EtZ")
auth.set_access_token("989062603-pChjdoZDHY8YsklhXaGft5unmvnwrObiY9FwOLMY", "tDnHKBDUx3CRt8CPkmiNg5MPl9eSnND3RobaQx2NSyrDs")
stream = Stream(auth, listener_producer)
stream.filter(languages=["en"], track=["trump"])
