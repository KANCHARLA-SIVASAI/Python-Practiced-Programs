#1.Write a python programm Which will accept a value and decide whether it is a polindrom or not
s=input()
result= "is polindrom" if s == s[::-1] else "is not polindrom"
print(s,result)