from collections import Counter
def values(stvalue:str)->int:
    counter=Counter(stvalue)
    cn=0
    for i in counter.values():
        k=i-1
        while k>=1:
            cn+=k
            k-=1
    # print(counter)q
    return len(stvalue)+cn
    
    
stvalue=input("enter the string: ")
k=values(stvalue)
print(k)

