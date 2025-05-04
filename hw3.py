#Python program  to find length of list
l=input("Enter input data:").split()
print("List:",l)
print(f"length of list using len()={len(l)}")
length=0
for x in l:
    length=length+1
print(f"Length of list without using len()={length}")