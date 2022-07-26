#coding:utf-8

import os

user = os.getlogin()
path = "/Users/" + user + "/Desktop"
os.chdir(path)

with open("myFile.txt", "w") as f:
    f.write("Python est un langage de programmation souple et flexible.\n")
    
with open("myFile.txt", "a") as f:
    f.write("Ce contenu a été ajouté via un code Python !\n")
