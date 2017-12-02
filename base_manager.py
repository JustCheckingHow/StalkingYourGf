

import os
import datetime
from friends_analyzis import *
#import codecs



s = "fb_id:\nmail:\nplec:\nimie:\nnazwisko:\ndata_urodzenia_fb:\ndata_urodzenia_znana:\nnumer_tel:\nmiasto_urodzenia:\nmiejsce_zamieszkania:\nzwiazek:\nnauka:\nprofile_img_src:\n"

def person_in_base(fbid): #if there is no person i base
	f = open("base/in_base", "r")
	data = f.read()
	if data.find(fbid) == -1:
		return 0
	return 1

def add_differences(name, f_list):
	'''
	TUTAJ KOD DO ROZNIC
	
	'''

def create_folder(fbid):
	path = "mkdir base/" + fbid
	f = os.popen(path)
	now = f.read()
	if now.find("mkdir")==1:
		print(fbid)
		print("    unable to create direcotry: ", now)
		return 0 
	return 1

def create_person_files(fbid): #and deleted
	path = "touch base/" + fbid + "/" + fbid + "_friends"

	f = os.popen(path)
	now = f.read()
	if now.find("mkdir")==1:
		print(fbid)
		print("    unable to create file friends_base: ", now)
		return 0
	
	path = "touch base/" + fbid + "/" + fbid + "_likes"

	f = os.popen(path)
	now = f.read()
	if now.find("mkdir")==1:
		print(fbid)
		print("    unable to create file friends_likes: ", now)
		return 0
	
	
	path = "touch base/" + fbid + "/" + fbid + "_friends_deleted"
	
	f = os.popen(path)
	now = f.read()
	if now.find("mkdir")==1:
		print(fbid)
		print("    unable to create file friends_deleted: ", now)
		return 0
	
	
	path = "touch base/" + fbid + "/" + fbid + "_friends_added"
	
	f = os.popen(path)
	now = f.read()
	if now.find("mkdir")==1:
		print(fbid)
		print("    unable to create file friends_added: ", now)
		return 0
	
	return 1

def convert_name(name):  #gettin rid of big letters and special letters by trolls on fb
	name = name.replace(" ", "_")
	name = name.replace("/", "_")
	name = name.replace("\\", "_")
	name = name.replace(".", "_")
	
	#name = name.replace("", "_")
	name = name.lower()
	return name

def create_person_overview(fbid): #creates person_overview file
	path = "touch base/" + fbid + "/" + fbid
	f = os.popen(path)
	now = f.read()
	if now.find("mkdir")==1:
		print(fbid)
		print("    unable to create overview: ", now)
		return 0

	path = "base/" + fbid + "/" + fbid
	f = open(path, "w")
	f.write(s)
	f.close()
	return 1

def create_person(fbid):
	
	#print("Creating person: " + name)
	
	
	if person_in_base(fbid) == 1:
		print("Already in base!")
		return 0
	
	if create_folder(fbid) != 1:
		print("error creating folder")
		exit(0)
	
	if create_person_files(fbid) != 1:
		print("error creating files")
		exit(0)

	if create_person_overview(fbid) != 1:
		print("error creating overview")
		exit(0)
	
	#print name
	
	string = (fbid +"\n")
	
	f = open("base/in_base", "a")
	f.write(string)
	f.close()
	
	
	return 1
	

def save_person_friends(fbid, friends_str):
	path = "base/" + fbid + "/" + fbid + "_friends"
	f = open(path, "w")
	f.write(friends_str)
	f.close()
	
def save_person_likes(fbid, likes_str):
	path = "base/" + fbid + "/" + fbid + "_likes"
	f = open(path, "w")
	f.write(likes_str)
	f.close()


	
################################################################################

def base_save_id(fbid):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()

	if data.find("fb_id:\n") !=-1:
		data = data[0:6] + fbid + data[6:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

'''def base_read_id(name):
	name = convert_name(name)
	path = "base/"+name+"/"+name
	f = open(path,"r")
	data = f.read()
	f.close()
	poz = data.find("fb_id:\n")
	if poz ==-1:
		print(data[poz+6:data.find("\n")]	'''

def base_save_mail(fbid, mail):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("mail:\n")
	if poz !=-1:
		data = data[0:poz+5] + mail + data[poz+5:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_plec(fbid, plec):
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("plec:\n")
	if poz !=-1:
		data = data[0:poz+5] + plec + data[poz+5:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_imie(fbid, imie):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("imie:\n")
	if poz !=-1:
		data = data[0:poz+5] + imie + data[poz+5:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_nazwisko(fbid, nazwisko):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("nazwisko:\n")
	if poz !=-1:
		data = data[0:poz+9] + nazwisko + data[poz+9:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_data_urodzenia_facebook(fbid, data_urodzenia_fb):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("data_urodzenia_fb:\n")
	if poz !=-1:
		data = data[0:poz+18] + data_urodzenia_fb + data[poz+18:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_data_urodzenia_znana(fbid, data_urodzenia_znana):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("data_urodzenia_znana:\n")
	if poz !=-1:
		data = data[0:poz+21] + data_urodzenia_znana + data[poz+21:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()		

def base_save_numer_tel(fbid, numer_tel):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("numer_tel:\n")
	if poz !=-1:
		data = data[0:poz+10] + numer_tel + data[poz+10:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_miasto_urodzenia(fbid, miasto_urodzenia):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("miasto_urodzenia:\n")
	if poz !=-1:
		data = data[0:poz+17] + miasto_urodzenia + data[poz+17:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_miejsce_zamieszkania(fbid, miejsce_zamieszkania):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("miejsce_zamieszkania:\n")
	if poz !=-1:
		data = data[0:poz+21] + miejsce_zamieszkania + data[poz+21:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_zwiazek(fbid, zwiazek):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("zwiazek:\n")
	if poz !=-1:
		data = data[0:poz+8] + zwiazek + data[poz+8:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()

def base_save_nauka(fbid, nauka):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("nauka:\n")
	if poz !=-1:
		data = data[0:poz+6] + nauka + data[poz+6:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()
		
def base_save_profile_img_src(fbid, src):
	
	path = "base/"+fbid+"/"+fbid
	f = open(path, "r")
	data = f.read()
	f.close()
	poz = data.find("profile_img_src:\n")
	if poz !=-1:
		data = data[0:poz+16] + src.encode("utf-8") + data[poz+16:]
		#print(data),
		f = open(path, "w")
		f.write(data)
		f.close()
##############################################################################






