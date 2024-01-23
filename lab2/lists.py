#ex 1-8
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#2
fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi"
print(fruits)
#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)
#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5]) #The search will start at index 2 (included) and end at index 5 (not included).
#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#EXAMPLES
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)