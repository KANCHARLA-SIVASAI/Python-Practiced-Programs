#9.write a python program which will accept a word from keyboard and decide whether it is vowel word or not
str=input()
result='is a vowel word' if [char for char in str if char in "aeiou"] else 'is not a vowel word'
print(str,result)