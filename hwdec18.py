#write a python program which will calculate area of square,rectagle,circle,triangle by using functions
import math
print("*"*50)
print("*"*50)
def Area_Of_Square():
    a=float(input("Enter value of side of square:"))
    print("area of square=",a**2)

def Area_Of_Rectangle():
    l=float(input("Enter value of length of rectangle:"))
    b=float(input("Enter value of breadth of rectangle:"))
    print("area of reactangle=",l*b)
def Area_Of_Circle():
    r=float(input("Enter value of radius of circle:"))
    print("area of circle=",math.pi*r**2)
def Area_Of_Triangle():
    b = float(input("Enter value of base of triangle:"))
    h = float(input("Enter value of height of triangle:"))
    print("area of triangle=",0.5*b*h)

Area_Of_Square()
print("*"*50)
Area_Of_Rectangle()
print("*"*50)
Area_Of_Circle()
print("*"*50)
Area_Of_Triangle()
print("*"*50)
print("*"*50)
