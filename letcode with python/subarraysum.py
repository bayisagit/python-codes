def values(vak:list,k:int)->int:
    cn=0
    csu=0
    csd={0:1}
    for num in vak:
        csu+=num
        if (csu-k) in csd:
            cn+=csd[csu-k]
        if csu in csd:
            csd[csu]+=1
        else:
            csd[csu]=1
    return cn
    

vak=list(map(int,input("enter the numbers: ").split()))
k=int(input("enter the k value: "))
d=values(vak,k)
print(d)