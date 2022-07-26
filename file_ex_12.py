#coding utf-8
"""Écrire un programme en Python qui permet de créer un fichier nommé myFile.txt et d'ajouter le texte suivant: T = "learning to program in python is easier than learning to program in java"
Ecrire un programme en python qui permet de compter la fréquence de répétition de chaque mot qui se trouve sur le fichier myFile.txt"""

import os

user = os.getlogin()
my_path = "/Users/" + user + "/Desktop"
    
def firstQuestion(path):
    os.chdir(path)
    text = "learning to program in python is easier than learning to program in java"

    with open("monfichier.txt", "w") as f:
        f.write(text)

def secondQuestion(path):
    os.chdir(path)       

    with open("monfichier.txt", "r") as f:
        word_list = []
        a = f.read()
        a_split = a.split(" ")
        print(a_split)

        for i in a_split:
            word_count = a_split.count(i)
            if i not in word_list:
                word_list.append(i)
                print(f"Le mot '{i}' apparaît {word_count} fois dans le fichier")
