#ex 1-5
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)



