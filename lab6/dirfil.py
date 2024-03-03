import os
import string
#1EX
mypath="C:\\Users\\Lenovo\\Desktop\\python"
def listofdir(path):
    dirlist=[d for d in os.listdir(path) if os.path.isdir(d)]
    return dirlist        

print(listofdir(mypath))
print()
"""def listoffiles(path):
    for f in os.listdir(path):
        if os.path.isfile(f):
            print(f)"""

def listoffiles(path):
    listfiles=[ f for f in os.listdir(path) if os.path.isfile(f)]
    return listfiles
     
print(listoffiles(mypath))
print()

def allfd(path):
    print(os.listdir(path))
allfd(mypath)   

#2EX


def checkaccess(path):
   
    if os.path.exists(path):
        print(f"The path '{path}' does  exist.")
        
    
    
    if os.access(path, os.R_OK):
        print(f"The path '{path}' is readable.")
    else:
        print(f"The path '{path}' is not readable.")
    
   
    if os.access(path, os.W_OK):
        print(f"The path '{path}' is writable.")
    else:
        print(f"The path '{path}' is not writable.")
    
 
    if os.access(path, os.X_OK):
        print(f"The path '{path}' is executable.")
    else:
        print(f"The path '{path}' is not executable.")

checkaccess(mypath)

#3EX

def finder(path):
    if os.path.exists(path):
        print("Its exist:")
        print(os.listdir(path))
    else:
        print("doesnt exist")    
finder(mypath) 

#4EX
file = open("C:\\Users\\Lenovo\\Desktop\\python\\lab6\\myfile.txt").readlines()
linecount=0
for line in file:
    linecount += 1

print(linecount)    

#5Ex
mylist = list(input().split())
filepath="C:\\Users\\Lenovo\\Desktop\\python\\lab6\\myfile.txt"
def writer(myfile, list):
    with open(myfile, 'a') as file:
        for i in list:
            file.write(str(i)+" ")
            

writer(filepath,mylist)

#6EX
mypath="C:\\Users\\Lenovo\\Desktop\\python\\lab6\\fromAtoZ"
def generate_text_files(path):
    os.chdir(path)
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {letter}.txt")
            
generate_text_files(mypath)

#7EX
sourcef="C:\\Users\\Lenovo\\Desktop\\python\\lab6\\myfile.txt"
destfi="C:\\Users\\Lenovo\\Desktop\\python\\lab6\\destination.txt"
def copy_file(sourcefile, tocopy):
    
    with open(sourcefile, 'r') as source, open(tocopy, 'w') as destination:
         
        content = source.read()
            
        destination.write(content)
copy_file(sourcef, destfi)

#8EX
path="C:\\Users\\Lenovo\\Desktop\\python\\lab6\\fromAtoZ\\A.txt"
def delete_path(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return 0

    os.remove(path)
    print("Deleted")

delete_path(path)
            







            