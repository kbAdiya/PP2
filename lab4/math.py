import math
#1EX
def detorad(degree):
    rad=degree*(math.pi/180)
    return rad
de=float(input())
print(detorad(de))    
#or
degree = int(input("Input degree: "))
print("Output radians:", math.radians(degree))

#2EX
def ar(h,b,a):
    area=float((b+a)*0.5*h)
    return area
height=int(input("height: "))
base1=int(input("Base1: "))
base2=int(input("Base2: "))
print(ar(height,base1,base2))

#3EX
def polygon_area(n, s):
    area = int((n * s ** 2) / (4 * math.tan(math.pi / n)))
    return area

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
print("The area of the polygon is:", polygon_area(n, s))

#4EX
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
print(float(base * height))
