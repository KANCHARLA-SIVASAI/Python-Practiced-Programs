#8.write a python program which will accept a letter and decide whether it is vowel or consonent
l=input().lower()
result='is vowel' if l in ['a','e','i','o','u'] else 'is consonent'
print(l,result)