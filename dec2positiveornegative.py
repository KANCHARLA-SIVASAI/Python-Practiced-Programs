#7.write a python program which will accept a numerical value and decide whether it is positive or negative number
a=float(input())
result='number is a positive number' if a>0 else 'number is a negative number' if a<0 else 'number is 0'
print(result)
