from collections import Counter
def calvale(strva:str,v:int)->int:
    counter=Counter()
    i=0
    ans=0
    for u,j in enumerate(strva):
        counter[j] +=1
        while len(counter) > v:
            counter[strva[i]]-=1
            if counter[strva[i]] == 0:
                counter.pop(strva[i])
            i+=1
        ans=max(ans,u-i+1)
    return ans
    
    
strva=input("enter the string")
v=int(input("with how many max different numbers: "))
k=calvale(strva,v)

print(k)