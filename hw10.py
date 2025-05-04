#Python program to find largest number in a list
l=input("Enter List Elements:").split()
l.sort()
print("Largest Element in the List:{}".format(l[-1]))