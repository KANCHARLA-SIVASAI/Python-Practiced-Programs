#areas of different figures using match case
import math as m
import sys as s
print("*"*50)
print("\t\tR. Rectangle")
print("\t\tS. Square")
print("\t\tC. Circle")
print("\t\tT. Triangle")
print("\t\tE. Exit")
print("*"*50)
ch=input("\t\tEnter Ur Choice:")
match(ch.upper()):
    case "R":
        l,b=float(input("Enter Value of length:")),float(input("Enter Value of Breadth:"))
        print("Area of Rectangle= {}".format(l*b))
    case "S":
        a=float(input("enter value of side of square:"))
        print("Area of Square= {}".format(a*a))
    case "C":
        r=float(input("Enter Value of Radius of Circle:"))
        print("Area Of Circle= {}".format(m.pi*r**2))
    case "T":
        b,h=float(input("enter value of base of triangle:")),float(input("enter value of height of triangle:"))
        print("Area Of Triangle= {}".format(0.5*b*h))
    case "E":
        s.exit()
    case _:
        print("You Chosen Wrong Choice!")