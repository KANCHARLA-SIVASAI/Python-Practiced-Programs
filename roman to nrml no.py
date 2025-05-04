#6.Write a python program which will convert roman number to normal number
print("*"*50)
roman=input("Enter Roman Number:")
d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
res=0
for i in range(len(roman)):
    if(i>0 and d[roman[i]]>d[roman[i-1]]):
        res=res+d[roman[i]]-2*d[roman[i-1]]
    else:
        res=res+d[roman[i]]
print("Value of roman numerical {} = {}".format(roman,res))
print("*"*50)
