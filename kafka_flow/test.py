import kafka
import time
import requests
import logging
logging.basicConfig(level='INFO')
consuming_host = '192.168.43.138:9092'
producing_host = '192.168.43.138:9092'
#
# consumer = kafka.KafkaConsumer('Receiver', bootstrap_servers=producing_host)

producer = kafka.KafkaProducer(bootstrap_servers=consuming_host)
URLS = ["https://www.facebook.com/search/4/photos-tagged"]
for url in URLS:
    print("CURRENTLY PARSING {}".format(url))
    r = requests.get(url).text
    p = len(r)
    a = 0
    stride = 8*200
    b = stride
    counter = 0
    while True:
        bytes_str = r[a:b].encode()
        counter += 1
        producer.send('nifiTest', bytes_str).get(timeout=30)
        a = b
        b = b + stride
        if counter >= p:
            break
