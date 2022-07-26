#coding: utf-8
#Ecrire un programme Python qui permet de regrouper dans une liste les mots communs à deux fichiers textes : fichier1.txt et fichier2.txt.

import os

user = os.getlogin()
my_path = "/Users/" + user + "/Desktop"

os.chdir(my_path)       
with open("fichier1.txt", "r") as f:
    a = f.read()
    a_split = a.split()
    with open("fichier2.txt", "r") as g:
        common_word = []
        b = g.read()
        b_split = b.split()
        print(b_split)
        print(a_split)
        for word in a_split:
            if word in b_split and word not in common_word:
                common_word.append(word)
        print(common_word)

