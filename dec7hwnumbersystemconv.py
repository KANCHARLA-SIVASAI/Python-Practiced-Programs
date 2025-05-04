#number system converting calculator
print("*" * 50)
print("\t\t\tBase Conversion Calculator")
print("*" * 50)
print("\t\t1.D To B \n\t\t  D To O \n\t\t  D To H")
print("*" * 50)
print("\t\t2.B To D \n\t\t  B To O \n\t\t  B To H")
print("*" * 50)
print("\t\t3.O To D \n\t\t  O To B \n\t\t  O To H")
print("*" * 50)
print("\t\t4.H To D \n\t\t  H To B \n\t\t  H To O")
print("*" * 50)
ch = int(input("Choose your choice: "))
match ch:
    case 1:
        d = int(input("Enter a decimal number: "))
        print("Binary: {}".format(bin(d)))
        print("Octal: {}".format(oct(d)))
        print("Hexadecimal: {}".format(hex(d)))

    case 2:
        b = input("Enter a binary number: ")
        d = int(b, 2)
        print("Decimal: {}".format(d))
        print("Octal: {}".format(oct(d)))
        print("Hexadecimal: {}".format(hex(d)))

    case 3:
        o = input("Enter an octal number: ")
        d = int(o, 8)
        print("Decimal: {}".format(d))
        print("Binary: {}".format(bin(d)))
        print("Hexadecimal: {}".format(hex(d)))

    case 4:
        h = input("Enter a hexadecimal number: ")
        d = int(h, 16)
        print("Decimal: {}".format(d))
        print("Binary: {}".format(bin(d)))
        print("Octal: {}".format(oct(d)))
    case _:
        print("please choose valid choice!")
