# Write a python program which will implement the following:
# ex:d={10:"Python",20:"Java",30:"Django",40:"DSA",50:"AI"}
# Get the Name of the Course whose Course name length lies between 2 to 3
print("-"*100)
print("-"*100)
n = int(input("\tEnter the number of items: "))
d = {}
for i in range(n):
    key = input("\tEnter key: ")
    value = input("\tEnter value: ")
    d[key] = value
print("-"*100)
print("\tGiven Items: ",d)
res=list(filter(lambda s:len(s) in [2,3],d.values()))
print("\tNames of the Courses whose Course name length lies between 2 to 3: ",res)
print("-"*100)
print("-"*100)
