import kafka
import time
import requests
import logging
logging.basicConfig(level='INFO')
consuming_host = '192.168.43.138:9092'
producing_host = '192.168.43.138:9092'
producing_host = '192.168.43.61:9093'
consumer = kafka.KafkaConsumer('test', bootstrap_servers=[producing_host])
producer = kafka.KafkaProducer(bootstrap_servers=producing_host)
for msg in consumer:
    print(msg)
    fbid = msg[0].value
    uid = msg[1].value

    const_url = b"https://www.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={}&av={}".format(fbid, uid)
    producer.send('nifiTest', const_url).get(timeout=30)
