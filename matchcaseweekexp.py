#areas of different figures using match case
import sys as s
print("*"*50)
d=input("\t\tEnter Weekday:")
match(d.upper()):
    case "MONDAY":
         print("{} is Working Day".format(d))
    case "TUESDAY":
        print("{} is Working Day".format(d))
    case "WEDNERSDAY":
        print("{} is Working Day".format(d))
    case "THIRSDAY":
        print("{} is Working Day".format(d))
    case "FRIDAY":
        print("{} is Working Day".format(d))
    case "SATURDAY":
        print("{} is Week End".format(d))
    case "SUNDAY":
        print("{} is  Holyday".format(d))
    case "E":
        s.exit()
    case _:
        print("Not A Weekday")