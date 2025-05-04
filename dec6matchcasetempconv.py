#Temperature conversions using match case keywords
import sys as s
print("*"*50)
print("\t\t1. F to C")
print("\t\t2. F to K")
print("\t\t3. C to F")
print("\t\t4. C to K")
print("\t\t5. K to F")
print("\t\t6. K to C")
print("\t\t7. Exit")
print("*"*50)
ch=int(input("\t\tEnter Ur Choice:"))
match(ch):
    case 1:
        f=float(input("\t\tEnter Value Of Temperature in Fahrenheit:"))
        print("\t\tTemperature in Celcius= {}".format((f-32)*(5/9)))
    case 2:
        f = float(input("\t\tEnter Value Of Temperature in Fahrenheit:"))
        print("\t\tTemperature in kelvin= {}".format((f - 32) * (5 / 9)+273.15))
    case 3:
        c = float(input("\t\tEnter Value Of Temperature in Celcius:"))
        print("\t\tTemperature in Farhenheit= {}".format(c*(9/5)+32))
    case 4:
        c = float(input("\t\tEnter Value Of Temperature in Celcius:"))
        print("\t\tTemperature in kelvin= {}".format(c+273.15))
    case 5:
        k=float(input("\t\tEnter Value Of Temperature in Kelvins:"))
        print("\t\tTemperature in Celcius= {}".format(k-273.15))
    case 6:
        k=float(input("\t\tEnter Value Of Temperature in Kelvins:"))
        print("\t\tTemperature in Farhenheit= {}".format((k-273.15)*(9/5)+32))
    case 7:
        s.exit()
    case _:
        print("\t\tYou Chosen Wrong Choice!")