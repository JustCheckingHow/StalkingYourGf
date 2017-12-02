import kafka
import time
import requests
import logging
logging.basicConfig(level='INFO')
consuming_host = '192.168.43.138:9092'
producing_host = '192.168.43.138:9092'
consumer_topic = 'PHOTOSid'

id_consumer = kafka.KafkaConsumer(bootstrap_servers=producing_host)
id_consumer.subscribe([consumer_topic])
while True:
    sent = True
    while sent:
        for msg in id_consumer:
            total_msg = str(msg.value)
            print(total_msg)
            sent = False
            break
    total_msg = total_msg.split(';')[0].split('|').replace('b\'','')
    uid = total_msg[0]
    fbid = total_msg[1]
    topic = total_msg[2]
    const_url = b"https://www.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={}&av={}".format(fbid, uid)
    producer.send(topic, const_url).get(timeout=30)
