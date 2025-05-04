import functools
l=list(map(float,input("Enter List Of Elements:").split()))
s=functools.reduce(lambda x,y:x if x<y else y,l)
b=functools.reduce(lambda x,y:x if x>y else y,l)
print("smallest number: ",s)
print("biggest number: ",b)