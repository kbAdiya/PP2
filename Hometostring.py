#comment 
print("Hello, World!")
#Python uses indentation to indicate a block of code
if 5 > 2:
  print("YES")
"""
This is a comment
written in
more than just one line
"""  
"""A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords."""
x = 50 # int type
print(x)
y= 10
z=x+y
print(x+y)
print(z)

carname = "Volvo" #str
print(carname)
print("50 type: ", type(x))
print("volvo type: ", type(carname))

t,w = "John","CARL"
print(t+w)

print("/////")
x = "awesome" #global

def myfunc():
  x = "fantastic" #local
  print("Python is " + x)

myfunc()

print("Python is " + x)



def myfunc():
  global x   #to make it global to use it outside of function
  x = "fantastic"

myfunc()

print("Python is " + x)

#data types:
print("//////")
x=20.5
print(type(x)) #float
x = ["apple", "banana", "cherry"]
print(type(x)) #list
x = ("apple", "banana", "cherry")
print(type(x)) #tuple
x = {"name" : "John", "age" : 36}
print(type(x)) #dict
x = True
print(type(x)) #bool
x = 3+5j
print(type(x)) #complex
print("///////")
#Convert from one type to another:(You cannot convert complex numbers into another number type.)
x=5.5
print("before: " ,type(x))
x=int(x)
print("after: ", type(x))
x=complex(x)
print(type(x))
print("/////")

x = "Hello World"
print("len of hello world is ", len(x))
b = "Hello, World!"
print("characters from position 2 to position 5 (not included) are: ", b[2:5])
b = "Hello, World!"
print(b[2:])
#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
print(x)
txt = "Hello World"
txt = txt.upper()
print(txt)
txt="HELLO"
print(txt.lower())
txt = "Hello World"
txt = txt.replace("H", "J") #using replace


print(txt)
a = "Hello, World!"
print(a.split(","))
""" we cannot combine strings and numbers so 
The format() method takes the passed arguments, 
formats them, and places them in the string where the placeholders {} are:"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
txt = 'It\'s alright.'
print(txt) 
