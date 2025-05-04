#Write a python program which will accept list of values which contains numbers and words. Get the words which contains atleast one vowel and whose length ranges between 3 to 4
def vowelword(word):
    flag=False
    for letter in word:
        if(letter in "aeiou" and len(word) in [3,4]):
            flag=True
            return word
            break
l=input("Enter list of values which contains numbers and words:").split()
print("list elements are:",l)
res=list(filter(vowelword,l))
print(res)
