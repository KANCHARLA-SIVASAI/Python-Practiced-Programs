#Python Program to Count occurrences of an element in a list
l=input("Enter List Elements:").split()
n=input("Enter Element To Count Ocuurences:")
count=0
for x in l:
    if(x==n):
        count=count+1
print("Occurence of {} in {} = {}".format(n,l,count))
