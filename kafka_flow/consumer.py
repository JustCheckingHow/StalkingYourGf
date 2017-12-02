
from kafka import KafkaConsumer
import logging
logging.basicConfig(level='INFO')

consumer = KafkaConsumer('test', group_id=None, api_version=(0,10))
for msg in consumer:
    print (msg)
