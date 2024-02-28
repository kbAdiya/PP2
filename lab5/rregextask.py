import re
file = open("C:\\Users\\Lenovo\\Desktop\\python\\lab5\\rowtask.txt").readlines()
#1ex
pattern = re.compile("[a]{1}[b]*")

    
for line in file:
       
    for word in line.split():
           
        if pattern.match(word):
               
            print(word)
print()

#2ex
pattern2 = re.compile("[a]{1}[b]{2,3}")   

    
for line in file:
       
    for word in line.split():
           
        if pattern2.match(word):
               
            print(word)
print()

#3ex
pattern3 = re.compile("[a-z]+[_]{1}[a-z]+")   

    
for line in file:
       
        for word in line.split():
           
            if pattern3.match(word):
               
                print(word)
print()
                
#4ex
pattern4 = re.compile("[A-Z]{1}[a-z]+")   

    
for line in file:
       
        for word in line.split():
           
            if pattern4.match(word):
               
                print(word)
print()

#5ex
pattern5 = re.compile("[a]+.+[b]$")   

    
for line in file:
       
        for word in line.split():
           
            if pattern5.match(word):
               
                print(word)
print()               

#6ex
pattern6 = re.compile("[ ,.]")   
with open("C:\\Users\\Lenovo\\Desktop\\python\\lab5\\rowtask.txt", "r") as file:
    
   for line in file:
        modified_line = pattern6.sub(':', line)
        print(modified_line, end="") 


print()
print()

 #7EX          
def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case


with open("C:\\Users\\Lenovo\\Desktop\\python\\lab5\\rowtask.txt", "r") as file:
    for line in file:
        camel_case_line = snake_to_camel(line.strip())
        print(camel_case_line)

print()

#8EX
pattern8 = re.compile('(?=[A-Z])')
with open("C:\\Users\\Lenovo\\Desktop\\python\\lab5\\rowtask.txt", "r") as file:
     for line in file:
       
        for word in line.split():
           print(re.split(pattern8, word), end=" ")

print()           

#9EX
pattern9 = re.compile('(?=[A-Z])')
with open("C:\\Users\\Lenovo\\Desktop\\python\\lab5\\rowtask.txt", "r") as file:
     for line in file:
       
        for word in line.split():
           modified_text = pattern9.sub( ' ', word)
           print(modified_text,)
print()

#10EX
pattern10 = re.compile('(?=[A-Z])') 
with open("C:\\Users\\Lenovo\\Desktop\\python\\lab5\\rowtask.txt", "r") as file:
     for line in file:
       
        for word in line.split():
           modified_text = pattern9.sub( "_", word).lower()
           print(modified_text, end=" ") 


file.close()            






                
