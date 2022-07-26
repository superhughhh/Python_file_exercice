#coding:utf-8

"""Écrire un programme Python permettant de créer un fichier nommé myFile.txt et d'y écrire le texte suivant:
"Python est le meilleur langage de programmation"
Écrire un programme Python qui supprime le 5ème mot du fichier myFile.txt"""


import os

user = os.getlogin()
path = "/Users/" + user + "/Desktop"
os.chdir(path)

text = "Python est un langage de programmation souple et flexible."
text_split = text.split(" ")
len_liste = len(text_split)
list_new_text = []
new_text = ""
print(len_liste)
for i in range(0, len_liste):
    if i != 4:
        list_new_text.append(text_split[i])

new_text = " ".join(list_new_text)


with open("Myfile.txt", "w") as f:
    f.write(new_text + "\n")
    


## Correction : 


 
# coding: utf-8
# ouvrire le fichier myFile.txt en mode lecture
f = open("myFile.txt" , 'r')
 
# récupération du contenu du fichier
content = f.read()
 
# transformation du contenu en une liste de mots
L = content.split()
 
# suppression du 5 ème mot
L.pop(4)
 
# recréation du contenu
f = open("myFile.txt" , 'w')
for mot in L:
    f.write(mot + " ")
    
f.close()
# maintenant si on ouvre le fichie, on y trouve la phrase:
# "Python est le meilleur de programmation" 