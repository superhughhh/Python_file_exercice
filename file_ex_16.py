
import os 


def head(path, n):
    with open(path, "r") as f:
            f_list = f.readlines()
            for i in range(0,n):
                print(f_list[i].strip('\n'))
            

def tail(path, n):
    with open(path, "r") as f:
            f_list = f.readlines()
            for i in range(1, n+1):
                print(f_list[-i].strip('\n'))
                
                
def copyAndRewrite(path, new_path):
    with open(path, "r") as f:
        f_list = f.readlines()
        copy_list = []
        for i in range(2, 5):
            copy_list.append(f_list[i])
            print(f_list[i])
    with open(new_path + "new_file.txt", "w") as f:
        for i in copy_list:
            f.write(i)
        
        
            
            
            
path = "/Users/admin/Desktop/monfichier.txt"
new_file_path = "/Users/admin/Desktop/"
head(path, 3)
tail(path, 3)
copyAndRewrite(path, new_file_path) 