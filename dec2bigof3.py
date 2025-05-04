#4.Write a python program which will accept three numerical values find the biggest among them and check for equality
a,b,c= float(input()),float(input()),float(input())
result=a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "equal numbers"
print(result)