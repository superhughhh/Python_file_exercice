#coding utf-8

"Ecrire un programme en Python permettant de supprimer les espaces multiples dans un fichier texte."


import os

user = os.getlogin()
my_path = "/Users/" + user + "/Desktop"


def CreateFile(path):
    os.chdir(path)
    text = "A    Text   with some   too       much      space"
    with open("monfichier.txt", "w") as f:
        f.write(text)

def RemoveExcessSpaces(path):
    os.chdir(path)       
    with open("monfichier.txt", "r") as f:
        a_list = []
        a = f.read()
        a_list = a.split()
        text_without_space = ""
        for word in a_list:
            text_without_space = text_without_space + word + " "
        print(text_without_space)

    with open("monfichier.txt", "w") as f:
        f.write(text_without_space)