#Python program to interchange first and last elements in a list
l=list(map(int,input("Enter List of Values:").split()))
l[0],l[-1]=l[-1],l[0]
print("After Interchanging 1st and last values in list New list=",l)