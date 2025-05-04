#Python program to print odd numbers in a list
l=input("Enter List Elements:").split()
res=[]
for x in l:
    if(int(x)%2!=0):
        res.append(x)
print("Odd Numbers in Givrn List= {}".format(res))