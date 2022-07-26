#coding: utf-8

import shutil
import os

user = os.getlogin()
path = "/Users/"+ user + "/Desktop"

os.chdir(path)

f = open("myFile.txt", "w")

os.mkdir("new")

shutil.move(path + "/myFile.txt", path + "/new/myFile.txt")
