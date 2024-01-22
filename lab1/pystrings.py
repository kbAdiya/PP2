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