#-*- coding: utf-8 -*-

import codecs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time as tm
from friends_parsing import *
from base_manager import *
from friends_analyzis import find_mutual_friends


def start_browser():
	browse = webdriver.Firefox()
	browse.get('http://facebook.com/')
	return browse

#############################################


def log_in(browse):
	# if ("Log" in browse.title):
	# clickLoginLink = browse.find_element_by_id("u_0_2")
	# clickLoginLink.click()

	mail_field = browse.find_element_by_id("email")
	mail_field.send_keys("witek1151@wp.pl")

	passwd = browse.find_element_by_id("pass")
	passwd.send_keys("Wants1^Perfect^Through")

	login_button = browse.find_element_by_id("loginbutton")
	login_button.click()
	# else:
		# print("already logged in");

#############################################
#assert "Facebook" in browse.title

def get_fbid_by_name(name, browse):
	chain = "http://facebook.com/search/top/?q="+name
	browse.get(chain)
	search = browse.find_element_by_xpath(".//*[@id='all_search_results']/div/div/div/div/a")
	search.click()
	#print("I am here!")

	url = browse.current_url

	#getting fb ID	#################
	poz = url.find("=")

	fbmail = ""
	if poz !=-1:
		fbmail = url[poz+1:]
	else:
		poz = url.rfind("/")
		fbmail = url[poz+1:]
	#################################


	#tm.sleep(1)

	#!!!!!!!!!!!!!!!!#tutaj pobieramy dane z tabelki miejsce zamieszkania itp.
	#get_table_info(browse, 0)
	#url = browse.current_url

	return fbmail

def search_friend_by_fbid(fbid, browse):
	chain = "http://facebook.com/"+fbid
	browse.get(chain)
	# search = browse.find_element_by_id("fb-timeline-cover-name")
	# search = search.get_attribute("innerHTML")
	# if search.find("<span")==-1:
	# 	return search
	# else:
	# 	return search[0:search.find("<span")-1]

#############################################
def goto_friends(browse):
	# dwie mozlowosci albo ktos ma mail facebookowy albo dziwny numer jak jest = to numer
	url = browse.current_url
	if url.rfind("=")==-1:
		chain = url + "/friends"
	else:
		chain = url + "&sk=friends"

	browse.get(chain)

def goto_likes(browse):
	# dwie mozlowosci albo ktos ma mail facebookowy albo dziwny numer jak jest = to numer

	url = browse.current_url
	url_p = url
	if url.rfind("=")==-1:
		chain = url + "/likes"
	else:
		chain = url + "&sk=likes"

	browse.get(chain)
	url = browse.current_url
	if url == url_p:
		return 0

	return 1

def scroll():
	value =0
	while 1:
		browse.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		old_val = value
		value = browse.execute_script("return window.scrollY;")
		#print(value)
		#print(old_val)
		if old_val == value :
			tm.sleep(5)
			browse.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			old_val = value
			value = browse.execute_script("return window.scrollY;")
			if old_val == value:
				break
		tm.sleep(0.7)

def get_friends_source(browse):
	source = browse.find_element_by_id('pagelet_timeline_medley_friends')
	source = source.get_attribute('innerHTML')
	with codecs.open("temps/temp_friends", "w", encoding='utf8') as f:
		f.write(source)
	f.close()

def get_likes_source(browse):
	source = browse.find_element_by_id('pagelet_timeline_medley_likes')
	source = source.get_attribute('innerHTML')
	with codecs.open("temps/temp_likes", "w", encoding='utf8') as f:
		f.write(source)
	f.close()

def get_table_info(browse, depth):

	if depth>5:
		print("get_table_info depth 6 reached check it!")
		browse.close()
		exit(0)

	try:
		source = browse.find_element_by_class_name("_1zw4")#(".//*[@id='u_jsonp_2_24']")
		source = source.get_attribute('innerHTML')
		with codecs.open("temps/temp_info_table", "w", encoding='utf8') as f:
			f.write(source)
		f.close()

	except NoSuchElementException:
		tm.sleep(1*(depth+1))
		#print("exception")
		get_table_info(browse, depth+1)

def get_profile_img(browse):
	search = browse.find_element_by_class_name("profilePicThumb")
	search = search.get_attribute("innerHTML")
	pocz = search.find('src=')
	src = search[pocz+5:search.find("\"", pocz+5)]
	return src

def get_person_likes(fbid, browse):
	search_friend_by_fbid(fbid, browse)
	if goto_likes(browse)==1:
		scroll()
		get_likes_source(browse)
		temp = parse_likes_data()
		return temp
		# save_person_likes(fbid, temp)


def get_person_friends(fbid, browse):
	search_friend_by_fbid(fbid, browse)
	goto_friends(browse)
	scroll()
	get_friends_source(browse)
	temp = parse_friends_data()
	return temp
	#save_person_friends(fbid, temp) commented by me

def save_basic_data(fbid, browse): #gets data from table and name and surname and puts it into info_file
	name = search_friend_by_fbid(fbid, browse)
	base_save_id(fbid)
	base_save_imie(fbid, name[0:name.find(" ")].encode("utf-8"))
	base_save_nazwisko(fbid, name[name.find(" ")+1:].encode("utf-8"))
	if name[name.find(" ")-1:name.find(" ")] == "a":
		base_save_plec(fbid, "female")
	else:
		base_save_plec(fbid, "male")

	get_table_info(browse, 0)
	parse_info_table(fbid)
	src = get_profile_img(browse)
	base_save_profile_img_src(fbid, src)


browse = start_browser()
log_in(browse)
fbid = "100001778185308"
tm.sleep(5)
#
# create_person(fbid)
# save_basic_data(fbid, browse)
# get_person_friends(fbid, browse)
# print(get_person_likes(fbid, browse))
name = search_friend_by_fbid(fbid, browse)
get_table_info(browse, 0) #not working
print(parse_info_table(fbid)) #not working


browse.close()
