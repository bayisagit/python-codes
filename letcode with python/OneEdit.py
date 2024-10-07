class Solution:
    def oneedit(self,w1:str,w2:str)->bool:
        m=len(w1)
        n=len(w2)
        if abs(m-n)>1:
            return False
        i,j,cnt = 0,0,0
        while i<m and j<n:
            if w1[i] != w2[j]:
                if cnt > 0:
                    return False
                if m>n:
                    i+=1
                elif m<n:
                    j+=1
                else:
                    i+=1
                    j+=1
                cnt+=1
            else:
                i+=1
                j+=1
        if i<m or j<n:
            cnt+=1
        return cnt == 1
            
    

w1=input("word1: ")
w2=input("word2: ")
solution=Solution()
ak=solution.oneedit(w1,w2)
print(ak)