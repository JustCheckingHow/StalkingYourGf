import kafka
import time
import requests
import logging
import os
from selenium import webdriver
print ("PLEASE ENTER MAIL AND PASSWORD BEFORE START")
mail = None
password = None
def start_browser():
	browse = webdriver.Firefox()
	browse.get('http://facebook.com/')
	return browse

def log_in(browse):
	mail_field = browse.find_element_by_id("email")
	mail_field.send_keys(mail)

	passwd = browse.find_element_by_id("pass")
	passwd.send_keys(password)

	login_button = browse.find_element_by_id("loginbutton")
	login_button.click()

logging.basicConfig(level='INFO')
browser = start_browser()
log_in(browser)

consuming_host = '192.168.43.138:9092'
producing_host = '192.168.43.138:9092'

url_consumer = kafka.KafkaConsumer(bootstrap_servers=producing_host)
consumer_topic = 'instructions'
url_consumer.subscribe([consumer_topic])
while True:
    url_tab = []
    sent = True
    while sent:
        for msg in url_consumer:
            url_tab = str(msg.value)
            print(url_tab)
            sent = False
            break
    url = url_tab.split('|')[0].replace('b\'', '')
    print("\nURL: ",url)
    topic = url_tab.split('|')[1].split(';')[0]
    print("\nTOPIC: ",topic)
    producer = kafka.KafkaProducer(bootstrap_servers=consuming_host)


    browser.get(url)
    time.sleep(5)
    sthm = browser.find_element_by_tag_name('body')
    string_to_send = sthm.get_attribute('innerHTML')

    r = string_to_send
    p = len(r)
    a = 0
    stride = 8*300
    b = stride
    counter = 0
    while True:
        bytes_str = r[a:b].encode()
        counter += stride
        producer.send(topic, bytes_str).get(timeout=30)
        a = b
        b = b + stride
        if counter >= p:
            break
