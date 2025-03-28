def cal(inp:list)->int:
    zer,l,k=0,0,1
    ans=0
    for i in range(len(inp)):
        if inp[i]==0:
            zer+=1
        while zer>k:
            if inp[l] == 0:
                zer-=1
            l+=1
        ans=max(ans,i-l+1)
    return ans
        
inp=list(map(int,input("enter the bit numbers: ").split()))
va=cal(inp)
print(va)