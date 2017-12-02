import kafka
import time
import requests
import logging
logging.basicConfig(level='INFO')
consuming_host = '192.168.43.138:9092'
producing_host = '192.168.43.138:9092'
consumer_topic = 'PHOTOS'

id_consumer = kafka.KafkaConsumer(bootstrap_servers=producing_host)
id_consumer.subscribe([consumer_topic])
producer = kafka.KafkaProducer(bootstrap_servers=consuming_host)
while True:
    sent = True
    while sent:
        for msg in id_consumer:
            total_msg = str(msg.value)
            print(total_msg)
            sent = False
            break
    total_msg = total_msg.split('|')[0]
    uid = total_msg[0].replace('b\'','')
    fbid = total_msg[1].replace('b\'','')
    topic = total_msg[2].replace('b\'','')
    const_url = "https://www.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={}&av={}".format(fbid, uid)
    producer.send(topic, const_url.encode()).get(timeout=30)
