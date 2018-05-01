#!/usr/bin/env python

from kafka import KafkaConsumer
import json
import pymongo
from pymonog import MongoClient
client = MongoClient()
db = client['twitter']
collection = db['TrumpTweets']
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('sri', group_id='sri', bootstrap_servers=['localhost:9092'])
for message in consumer:
    collection.insert_one(json.loads(message.decode('utf-8')))
