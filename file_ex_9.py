#coding:utf-8

"""1) - Écrire un programme en Python qui permet de créer un fichier nommé myFile.txt et d'ajouter les lignes suivantes:
Python Programming
Java Programming
C++ Programming
2) - Écrire un programme en Python qui permet d'échanger la troisième ligne avec la deuxième ligne du fichier myFile.txt."""

import os

def FirstQuestion():
    user = os.getlogin()
    path = "/Users/" + user + "/Desktop"
    os.chdir(path)


    list_language = ["Python", "Java", "C++"]
    new_text = "Programming"


    with open("Myfile.txt", "w") as f:
        for i in range(0,3):
            f.write(list_language[i] + " " + new_text + "\n")




def SecondQuestion():
    user = os.getlogin()
    path = "/Users/" + user + "/Desktop"
    os.chdir(path)   

    l_list = []

    with open("Myfile.txt", "r") as f: 
        content = f.readlines()
        for l in content:
            l_list.append(l)
        a = l_list[1]
        l_list[1] = l_list[2]
        l_list[2] = a


    print(l_list)
    with open("Myfile.txt", "w") as f:
        for i in range(0,3):
            f.write(l_list[i])

