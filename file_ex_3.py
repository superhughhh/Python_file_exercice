#coding:utf-8

import os 

user = os.getlogin()

os.chdir("/Users/" + user + "/Desktop")

f = open("myfile.txt", "w")

#actual name, new name
os.rename("myfile.txt","mytext.txt")

