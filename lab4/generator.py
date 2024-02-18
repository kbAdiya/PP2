#1Ex
def gen(n):
    for i in range(1,n+1):
        yield i*i
N=int(input())
for nums in gen(N):
    print(nums)

#2EX
def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
N=int(input())            
mylist=list(even(N))
print(*mylist, sep=",")    

#3EX
def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
for num in divisible(n):
    print(num)

#4EX
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("a: "))
b = int(input("b: "))
for square in squares(a, b):
    print(square)

#5EX
def tozero(n):
    while n>=0:
       yield n
       n-=1
N=int(input("N: "))
for nums in tozero(N):
    print(nums)    



