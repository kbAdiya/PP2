#1EX
import functools
list = map(int, list(input().split()))
print(functools.reduce(lambda x, y: x*y, list))

#2EX
string =input()
upper = sum(map(lambda x: x.isupper(), string))
lower = sum(map(lambda x: x.islower(), string))
print(f"Upper: {upper}, lower: {lower}")

#3EX
def is_palindrome(s):
    s = s.lower()
    if s==s[::-1]:
        return True
    else:
        return False    
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("palindrome.")
else:
    print("not a palindrome.")

#4EX
import time
import math

def delayed_square_root(number, delay_ms):
   
    delay_seconds = delay_ms / 1000
    
   
    time.sleep(delay_seconds)
    
  
    square_root = math.sqrt(number)
    
    return square_root


number = int(input("Enter the number: "))
delay_ms = int(input("Enter the delay in milliseconds: "))


print(f"Square root of {number} after {delay_ms} milliseconds is {delayed_square_root(number, delay_ms)}")

#5EX
def all_elements_true(tup):
    return all(tup)


my_tuple = (True, True, True)
print(all_elements_true(my_tuple)) 

my_tuple = (True, False, True)
print(all_elements_true(my_tuple)) 

        
