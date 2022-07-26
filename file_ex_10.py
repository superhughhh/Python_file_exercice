#coding:utf-8

"""Écrire un algorithme en Python qui permet de créer un fichier nommé myFile.txt et d'ajouter le texte: T = "Python est langage de programmation de haut niveau"
    Écrire un programme en Python qui transforme le contenu du fichier myFile.txt en écrivant chaque mot dans une ligne séparée."""

import os 

user = os.getlogin()
path = "/Users/" + user + "/Desktop"
os.chdir(path)

def FirstQuestion():
    text = "Python est langage de programmation de haut niveau"
    with open("Myfile.txt","w") as f:
        f.write(text)
 

def SecondQuestion():
    with open("Myfile.txt","r") as f:
        text = f.read()
        print(text)
        text_split = text.split(" ")

    with open("Myfile.txt","w") as f:
        for word in text_split:
            f.write(word + "\n")
 