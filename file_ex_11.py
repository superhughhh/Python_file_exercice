"""a) Ecrire un proramme qui permet de lister tous les dossiers du répertoire 'C:/Windows'
b) écrire un autre programme qui liste tous les fichiers du répertoire 'C:/Windows'.
c) En utilisant la méthode getlogin(), écrire un programme qui réalise les mêmes opérations pour le répertoire Desktop de l'utilisateur

"""


import os



def FirstQuestion(path):
    user = os.getlogin()
    path = "/Users/" + user
    os.chdir(path)

    ls = os.listdir()
    new_ls = []
    for i in ls:
        if "." not in i:
            new_ls.append(i)
    print(new_ls)
    
    
def SecondQuestion(path):
    os.chdir(path)

    ls = os.listdir()
    new_ls = []
    for i in ls:
        if "." in i and i[0] != ".":
            new_ls.append(i)
    print(new_ls)


user = os.getlogin()
user_path = "/Users/" + user
Desktop_path = "/Users/" + user

FirstQuestion(Desktop_path)
SecondQuestion(Desktop_path)