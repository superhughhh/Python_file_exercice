#coding:utf-8
#this program only work on MAC OS and Linux

import os 

#use this function to get login name
user = os.getlogin()

#I create a file and i rebuild the path
f = open("/Users/" + user + "/Desktop/monfichier.txt", "w")

#I write in the file txt
f.write("J'écris ce message depuis un script Python")

f.close()

###


f = open("/Users/" + user + "/Desktop/monfichier.txt", "r")

content = f.read()
print(content)


f.close()