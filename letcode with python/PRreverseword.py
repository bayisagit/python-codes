class Solution:
    def reverseword(self,wo:str):
        wo.strip()
        l=len(wo)
        um=wo.split()
        for j in range(len(um)-1,-1,-1):
            print(um[j],end=" ")
wo=input("Words: ")
sol=Solution()
c=sol.reverseword(wo)

    