#coding:utf-8

"""Ecrire un programme en Python qui affiche dans un fichier texte le mot le plus long et son nombre de caractère."""



import os

user = os.getlogin()
my_path = "/Users/" + user + "/Desktop"


def CreateFile(path):
    os.chdir(path)
    text = "Le langage python est le meilleur langage de programmation de tous les temps"
    with open("monfichier.txt", "w") as f:
        f.write(text)

#def RemoveExcessSpaces(path):
os.chdir(my_path)       
with open("monfichier.txt", "r") as f:
    a_list = []
    a = f.read()
    a_list = a.split()
    len_most_long_word = 0
    most_long_word = ""
    len_list = len(a_list)
    for i in range(0, len_list):
        len_word = len(a_list[i])
        if len_word > len_most_long_word:
            len_most_long_word = len_word
            most_long_word = a_list[i]
    print(f"le mot le plus long est '{most_long_word}' avec {len_most_long_word} caractères")
        

