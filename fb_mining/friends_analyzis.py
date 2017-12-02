def find_deletions(friends_file_path, new_friends_list):
	deleted = ""
	f1 = open(friends_file_path, "r")
	data2 = new_friends_list
	for line in f1:
		if data2.find(line) == -1:	
			print ("--" +line),
			deleted += line
	
	f1.close()
	return deleted
	
def find_additions(friends_file_path, new_friends_list):
	added = ""
	f2 = open(friends_file_path, "r")
	data1 = new_friends_list
	for line in f2:
		if data1.find(line) == -1:
			print ("++" +line),
			added += line
		
	f2.close()
	return added
	
def find_mutual_friends(path1, path2):
	f1 = open(path1, "r")
	f2 = open(path2, "r")
	
	data2 = f2.read()
	
	for line in f1:
		if data2.find(line) != -1:
			print ("mutuals: " + line),
	f1.close()
	f2.close()