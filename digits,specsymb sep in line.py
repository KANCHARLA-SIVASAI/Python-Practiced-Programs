#5.write a python program which will accept a line of text and get digits seperately and also get special symbols seperately
print("*"*50)
line=input("Enter A Line Of Text:")
if(line.isspace()):
    print("Invalid Input")
else:
    d=''
    sp=''
    for i in line:
        if(not i.isspace() and i.isdigit()):
            d=d+i
        if(not i.isspace() and not i.isdigit() and not i.isalpha()):
            sp=sp+i
    print("*" * 50)
    print("Only Digits Are:",d)
    print("Only Special Symbols Are:",sp)
    print("*" * 50)

