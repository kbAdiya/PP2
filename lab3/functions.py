
#ex1
def converter(grams):
    ounces = 28.3495231 * grams
    print(ounces)

grams_input = int(input("Enter the amount in grams: "))
converter(grams_input)


#ex2
Fahrenheit = float(input())

def FtoC(f):
    C = (5 / 9) * (f - 32)
    print(C)

FtoC(Fahrenheit)

#ex3
def solve(numheads, numlegs):
    x = numlegs - numheads * 2
    print("Rabbits:", x/2, "Chicken:", numheads - x/2)

solve(int(input("Heads:")), int(input("Legs:")))


#ex4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

mylist = list(map(int, input().split()))
for i in mylist:
    if is_prime(i):
        print(i)

#5
from itertools import permutations
a = str(input())
for perm in permutations(a, len(a)):
    print(''.join(perm))

#ex6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print(result)
#or
mylist = list(input().split())
def rev():
    newlist = list(reversed(mylist))
    print(*newlist)
rev()

#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33(list(map(int, input().split()))))
print(has_33([1, 3, 3]))      # True
print(has_33([1, 3, 1, 3]))   # False
print(has_33([3, 1, 3]))      # False
print()

#ex8
def spy_game(numer):
    pattern = [0, 0, 7]
    index = 0

    for num in numer:
        if num == pattern[index]:
            index += 1
            if index == len(pattern):
                return True

    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))   # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))   # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))   # False
print()
#or
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == nums[i+1] and nums[i] == 0 and nums[i+2] == 7:
            return True
        else:
            continue
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,7,2,0,4,5,0]))
print()


#ex9
import math
def sphere_volume(radius):
    if radius < 0:
        return "Radius cannot be negative."
    
    volume = (4 / 3) * math.pi * radius**3
    return volume

radius = float(input("Enter the radius of the sphere: "))
result = sphere_volume(radius)
print(result)
print()

#10
def unique_elements(input_list):
    result = []
    for element in input_list:
        if element not in result:
            result.append(element)
    return result


original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(original_list)
print(unique_list)
print()

#11
word=str(input())
def checker():
    new=word[::-1]
    if new==word:
        return True
    return False
if checker():
    print("Yes its palindrom")
else:
    print("no")    
print()

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
histogram([4, 9, 7])
#histogram(list(map(int, input().split())))

#ex13
import random

def guess_the_number():
  
    player_name = input("Hello! What is your name?\n")
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

   
    secret_number = random.randint(1, 20)

   
    guesses_taken = 0
    guessed_number = None

    while guessed_number != secret_number:
       
        guessed_number = int(input("Take a guess.\n"))

       
        guesses_taken += 1

        
        if guessed_number < secret_number:
            print("Your guess is too low.")
        elif guessed_number > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {guesses_taken} guesses!")


guess_the_number()

        
    