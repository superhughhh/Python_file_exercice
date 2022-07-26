#coding:utf-8

import os

user = os.getlogin()
path = "/Users/" + user + "/Desktop"
os.chdir(path)

f = open("myFile.txt", "w")

for i in range(1,6):
    f.write("Ligne numéro " + str(i) + "\n")
    if i == 3:
        f.write("désolé ! Le contenu de cette ligne a été changé !\n")