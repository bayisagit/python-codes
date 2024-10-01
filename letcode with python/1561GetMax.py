def piless(piles):
    piles.sort(reverse=True)
    n=len(piles)
    ans=[]
    for i in range(n//3):
        ans.append(piles[i*2+1])
    return ans
piles=[9,8,7,6,5,1,2,3,4]
result=piless(piles)
print(sum(result))

    