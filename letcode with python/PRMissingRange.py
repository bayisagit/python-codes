class Solution:
    def missingRange(self,k:list[int],l:int,u:int)->list[list[int]]:
        maxr=[]
        for n in range(len(k)-1):
            if k[n]+1 != k[n+1]:
                maxr.append([k[n]+1,k[n+1]-1])
        if k[-1]<u:
            maxr.append([k[-1]+1,u])
        return(maxr)
k = list(map(int,input().split()))
l,u = map(int,input().split())
solution=Solution()
du=solution.missingRange(k,l,u)
print(du)

        