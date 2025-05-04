#3.Write a python program which will accept two numerical values find the smallest among them and check for equality
a,b= float(input()),float(input())
result=a if a<b else b if b<a else "equal numbers"
print(result)