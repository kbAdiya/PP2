#Python syntax
print("////// ex1-2")
print("Hello, World!")
#Python uses indentation to indicate a block of code
if 5 > 2:
  print("YES")

print("////// python comments ex 1-2")
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

print("//// variavles ex 1-7")
carname = "Volvo" #str
print(carname)
x = 50 # int type
print(x)
print("50 type: ", type(x))
print("volvo type: ", type(carname))
x=5
y= 10
z=x+y
print(x+y)
print(z)
x,y,z="orange","banana","cherry"
print(x,y,z)
t=w = "John"
print(t,w)
print("/////")
x = "awesome" #global

def myfunc():
  x = "fantastic" #local
  print("Python is " + x)
myfunc()

print("Python is " + x)
print("///////")

def myfunc():
  global x   #to make it global to use it outside of function
  x = "fantastic"

myfunc()

print("Python is " + x)

#data types:
print("////// DATA TAPES EX 1-7")
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

print("/////// NUMBERS EX 1-3")
#Convert from one type to another:(You cannot convert complex numbers into another number type.)
x=5
x=float(x)
x=5.5
print("5.5 before: " ,type(x))
x=int(x)
print("5.5 after: ", type(x))
x=complex(x)
print(type(x))

print("///// STRING EX 1-8")
x = "Hello World"
print(x[0])
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
