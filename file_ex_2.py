import os

#this command allows to the progamm move in the good folder
os.chdir("/Users/admin/Desktop")

#not need to have the path in the open() function.
f = open("monfichier.txt", "w")


f.write("L'exercice 2 vient d'écraser ce que j'ai écris avec l'exercice 1")
f.close