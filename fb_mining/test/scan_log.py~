import datetime
import time as tm

#dd:mm:yyyy


def calc_diff(date):
	now = datetime.datetime.now()
	days = (int(now.day) - int(date[:2]))
	mont = (int(now.month) - int(date[3:5]))*30
	year = (int(now.year) - int(date[6:]))*365
	return days+mont+year


def next_person_to_scan():
	
	f = open("scan_log", "r")

	prev_poz = 0
	poz = 0


	maxi = 0
	maxi_name = ""
	for line in f:
		#print line,
		val = calc_diff(line[line.find(";")+1:line.find("\n")])
		if val > maxi:
			maxi = val
			maxi_name = line[:line.find(";")]

	print maxi_name
	

def set_person_as_scanned(fbid):
	f = open("scan_log", "r")
	data = f.read()
	#print(data),
	
	f.close()
	
	poz = data.find(fbid)
	if poz == -1:
		print("people to scan: no person in base: "+ fbid)
		return 0;
		
		
	end = data.find("\n", poz)
	data = data[0:poz]+data[end+1:] #\n zawiera 2 znaki trzeba oba usunac
	#print(data),
	f = open("scan_log", "w")
	
	f.write(data)
	f.close()
	return 1;

#next_person_to_scan()
set_person_as_scanned("dupci dupci")
