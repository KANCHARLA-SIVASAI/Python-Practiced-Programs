#Python program to print even numbers in a list
l=input("Enter List Elements:").split()
res=[]
for x in l:
    if(int(x)%2==0):
        res.append(x)
print("Even Numbers in Givrn List= {}".format(res))