import kafka
import time
import requests
import logging
import os
logging.basicConfig(level='INFO')
consuming_host = '192.168.43.138:9092'
producing_host = '192.168.43.138:9092'
#
# consumer = kafka.KafkaConsumer('Receiver', bootstrap_servers=producing_host)

producer = kafka.KafkaProducer(bootstrap_servers=consuming_host)
URLS = ["https://www.facebook.com/search/4/photos-tagged"]
mail = "witek1151@wp.pl"
password = "Wants1^Perfect^Through"
w_string = "wget \"https://www.facebook.com/search/4/photos-tagged\" --post-data \"email={}&pass={}\" --no-check-certificate --keep-session-cookies --save-cookies=cookies --load-cookies=cookies -U \"Mozilla/5.0 (Windows NT 5.2; rv:2.0.1) Gecko/20100101 Firefox/4.0.1\" -O test".format(mail, password)
print(w_string)
os.system(w_string)
with open('test', 'r') as f:
    string_to_send = f.read()

r = string_to_send
p = len(r)
a = 0
stride = 8*300
b = stride
counter = 0
while True:
    bytes_str = r[a:b].encode()
    counter += stride
    producer.send('nifiTest', bytes_str).get(timeout=30)
    a = b
    b = b + stride
    if counter >= p:
        break
