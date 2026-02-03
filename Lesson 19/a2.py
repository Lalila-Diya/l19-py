#word matching

def match(word):
    count=0
    list=[]
    for x in words:
        if x[0]==x[-1]:
            count+=1
            list.append(x)
    print("word matching are: ",list)
    return count

words=["aba","abc","xyz","121","1234567890987654321","madam","hello","civic"]
print("Words are: ",words)
print("Total word matching are: ",match(words))