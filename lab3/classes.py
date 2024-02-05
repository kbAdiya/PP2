
#ex1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())


string_manipulator = StringManipulator()
string_manipulator.getString()
string_manipulator.printString()
print()

#ex2
class Shape():
    def area(self):
        print("area equals 0")

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print("area equals", self.length**2)

print("Enter the length of your square:")
x = Square(int(input()))
a = Shape()
x.area()
a.area()
print()

#ex3
class Rectangle(Shape): 
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle_obj = Rectangle(5, 3)
print("Area of rectangle:", rectangle_obj.area())


#ex4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("(", self.x, ",", self.y, ")")

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self, other_point):
        distance = math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
        print("Distance is:", distance)

x_input = int(input("Enter x coordinate for the point: "))
y_input = int(input("Enter y coordinate for the point: "))
point = Point(x_input, y_input)

print("Coordinates are:")
point.show()

move_x = int(input("How do you want x to be moved? "))
move_y = int(input("And y? "))
point.move(move_x, move_y)

print("New coordinates:")
point.show()

x2_input = int(input("Enter x coordinate for the second point: "))
y2_input = int(input("Enter y coordinate for the second point: "))
second_point = Point(x2_input, y2_input)

point.dist(second_point)
print()

#ex5
class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds. Withdrawal canceled.")


account1 = Account("John Smith", 1000.0)
account1.deposit(500.0)
account1.withdraw(200.0)
account1.withdraw(900.0)
print()

#ex6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


numbers = list(map(int, input().split()))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)
#or
is_prime = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1

numbers_str = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, numbers_str.split()))

prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers:", prime_numbers)
 





