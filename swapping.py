#swapping of 2 nums
a,b=int(input()),int(input())
#syntax1
a,b=b,a
print("after first swap:",a,b)
#syntax2
a=a+b
b=a-b
a=a-b
print("after second swap:",a,b)
#syntax3
a=a^b
b=a^b
a=a^b
print("after third swap:",a,b)
#syntax4
t=a
a=b
b=t
print("after fourth swap:",a,b)
#syntax5
a=a*b
b=a//b
a=a//b
print("after fifth swap:",a,b)
