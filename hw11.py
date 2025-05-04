#Python program to find second largest number in a list
l=input("Enter List Elements:").split()
l.sort()
print("Second Largest Element in the List:{}".format(l[-2]))