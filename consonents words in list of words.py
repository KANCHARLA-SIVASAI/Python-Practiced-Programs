#Consonent words in list of words
l=input("enter words:").split()
for word in l:
    res=1
    for ch in word:
        if(ch.lower() in 'aeiou'):
            res=0
            break
    if(res):
        print(word)
