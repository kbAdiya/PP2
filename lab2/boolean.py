#ex 1-5
print(10>9) #true
print(10 == 9) #false
print(10 < 9) #false
print(bool("abc")) #true
print(bool(0)) #false

#examples
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))