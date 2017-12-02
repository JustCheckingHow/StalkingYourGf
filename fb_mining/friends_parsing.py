#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base_manager import *

def parse_friends_data():
	f = open("temps/temp_friends", "r")
	data = f.read()

	pocz = 0
	konc = 0
	prev = 0
	dane = ""
	for j in range(10000):


		pocz = data.find("fsl fwb fcb", pocz)
		#print pocz

		if prev > pocz:
			break

		pocz = data.find("<a", pocz)

		#get href value

		pocz = data.find("href=", pocz)
		pocz +=6

		############################################### GETTING FB ID

		konc = data.find("fref=pb", pocz)
		konc2 = data.find("&amp", pocz)
		if konc > konc2:
			konc = konc2
		else:
			konc-=1

		nickp = data.rfind("/", pocz, konc)+1
		nickp2 = data.rfind("=", pocz, konc)+1
		if nickp < nickp2:
			nickp = nickp2
		nick = ""

		for i in range(konc-nickp):
			nick += (data[nickp+i])

		###############################################

		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("<", pocz)


		wynik = ""
		for i in range(konc-pocz):
			wynik += (data[pocz+i])
		#print wynik+ ";" +nick
		pocz = konc
		prev = pocz
		dane += wynik+";"+nick+"\n"
		#print dane
	f.close()
	#print dane
	return dane


def parse_likes_data():
	f = open("temps/temp_likes", "r")
	data = f.read()

	pocz = 0
	konc = 0
	prev = 0
	dane = ""
	for j in range(10000):


		pocz = data.find("fsl fwb fcb", pocz)
		#print pocz

		if prev > pocz:
			break

		pocz = data.find("<a", pocz)

		#get href value

		pocz = data.find("href=", pocz)
		pocz +=6
		konc = data.find("\"", pocz)

		href = ""
		for i in range(konc-pocz):
			href += (data[pocz+i])


		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("<", pocz)


		wynik = ""
		for i in range(konc-pocz):
			wynik += (data[pocz+i])

		#print wynik, href
		pocz = konc
		prev = pocz
		dane += wynik+";"+href+"\n"
		#print wynik
	f.close()
	#print dane
	return dane

def parse_info_table(fbid):
	#fbid = convert_fbid(fbid)
	f = open("temps/temp_info_table", "r")

	data = f.read()

	#MIESZKA W:
	#print("Miasto zamieszkania:"),
	pocz = data.find("Mieszka w:")
	if pocz != -1:
		konc = data.find("</a", pocz)
		pocz = data.rfind(">", pocz, konc)
		pocz+=1
		#print(pocz, konc)
		wynik = ""
		for i in range(konc-pocz):
			wynik += (data[pocz+i])
		#print wynik
	else:
		wynik = "brak danych"
		#print ("brak danych")
	return wynik
	#base_save_miejsce_zamieszkania(fbid, wynik)


	#ZWIAZEK
	#print("Status:"),
	pocz = data.find("W związku z użytkownikiem")
	if pocz == -1:
		pocz = data.find("W związku")
		if pocz == -1:
			#print("brak danych")
			wynik = "brak danych"
		else:
			#print ("W związku!")
			wynik = "W związku!"

	else:
		konc = data.find("</a", pocz)
		pocz = data.rfind(">", pocz, konc)
		#print(pocz, konc)
		pocz +=1
		wynik =""
		for i in range(konc-pocz):
			wynik +=(data[pocz+i])
		#print wynik

	base_save_zwiazek(fbid, wynik)

	#DATA URODZENIA
	#print ("Data urodzenia:"),
	pocz = data.find("Data urodzenia:")
	if pocz == -1:
		#print ("brak danych")
		wynik = "brak danych"
	else:
		pocz = data.find(":", pocz)
		pocz +=2
		konc = data.find("<", pocz)
		wynik = ""
		for i in range(konc-pocz):
			wynik +=(data[pocz+i])
		#print wynik

	base_save_data_urodzenia_facebook(fbid, wynik)

	#MIEJSCE POCHODZENIA########################################################
	#print("Z:"),
	pocz = data.find("Z:")
	if(pocz == -1):
		#print("brak danych")
		wynik = "brak danych"
	else:
		konc = data.find("</a", pocz)
		pocz = data.rfind(">", pocz, konc)
		pocz +=1
		#print(pocz, konc)
		wynik =""
		for i in range(konc-pocz):
			wynik +=(data[pocz+i])
		#print wynik

	base_save_miasto_urodzenia(fbid, wynik)
	#NAUKA######################################################################

	#print ("NAUKA:"),

	pocz = data.find("Studiował na uczelni:")
	if pocz != -1:
		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("</a>", pocz)
		wynik =""
		for i in range(konc-pocz):
			wynik +=(data[pocz+i])

		#print wynik

	pocz = data.find("Studiowała na uczelni:")
	if pocz != -1:
		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("</a>", pocz)
		wynik =""
		for i in range(konc-pocz):
			wynik +=(data[pocz+i])

		#print wynik


	pocz = data.find("Studiuje na uczelni:")
	if pocz != -1:
		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("</a>", pocz)
		wynik =""
		for i in range(konc-pocz):
			wynik +=(data[pocz+i])

		#print wynik

	pocz = data.find("Studiował:") #...na
	if pocz != -1:
		pocz = data.find("na:", pocz)
		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("</a>", pocz)
		wynik =""
		for i in range(konc-pocz):
			wynik +=(data[pocz+i])

		#print wynik


	pocz = data.find("Studiowała") #...na
	if pocz != -1:
		pocz = data.find("na:", pocz)
		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("</a>", pocz)
		wynik =""
		for i in range(konc-pocz):
			wynik +=(data[pocz+i])

		#print wynik

	pocz = data.find("Studiuje:") #do skonczenia nadal
	if pocz != -1:
		konc = data.find("</a>", pocz)
		#print konc
		pocz1 = data.find(":", pocz)
		konc1 = data.find("<", pocz1)
		pocz1 +=2
		wynik1 = ""
		for i in range(konc1-pocz1):
			wynik1 +=(data[pocz1+i])

		#print wynik1,
		pocz2 = data.rfind(">", konc1, konc)
		pocz2+=1
		wynik2=""
		for i in range(konc-pocz2):
			wynik2 +=(data[pocz2+i])

		#print wynik2

	pocz = data.find("Uczęszczał do:")
	if pocz != -1:
		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("<", pocz)
		wynik =""

		for i in range(konc-pocz):
			wynik +=(data[pocz+i])

		#print wynik

	pocz = data.find("Uczęszczała do:")
	if pocz != -1:
		pocz = data.find(">", pocz)
		pocz +=1
		konc = data.find("<", pocz)
		wynik =""

		for i in range(konc-pocz):
			wynik +=(data[pocz+i])

		#print wynik
	if wynik=="":
		wynik = "brak danych"
	base_save_nauka(fbid, wynik)

#parse_friends_data()
