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