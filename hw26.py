#Python  Program to print duplicates from a list of integers
l=input("Enter List Elements:").split()
uniquelist=[]
duplicates=[]
for x in l:
    if x not in uniquelist:
        uniquelist.append(x)
    elif x not in duplicates:
        duplicates.append(x)
print("Duplicates in list are:",duplicates)