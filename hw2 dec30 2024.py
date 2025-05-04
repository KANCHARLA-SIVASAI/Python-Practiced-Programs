''' Write a python program which will implement the following
 a. Get all upper case alphabets in descending order
 b. Get all the lower case alphabets in ascending order
 c. Get all the odd numbers in ascending order
 d. Get all the even numbers in descending order
 Note:if any special symbols are there ignore them '''
print("-"*100)
print("-"*100)
l=input("\tEnter a word:")
print("-"*100)
res1=' '.join(sorted((filter(str.isupper,l)),reverse=True))
res2=' '.join(sorted((filter(str.islower,l))))
res3=' '.join(sorted((filter(lambda s :s.isdigit() and int(s)%2!=0,l))))
res4=' '.join(sorted((filter(lambda s :s.isdigit() and int(s)%2==0,l)),reverse=True))
print("\ta.All upper case alphabets in descending order:",res1)
print("\tb.Get all the lower case alphabets in ascending order:",res2)
print("\tc.Get all the odd numbers in ascending order:",res3)
print("\td.Get all the even numbers in descending order:",res4)
print("-"*100)
print("-"*100)
