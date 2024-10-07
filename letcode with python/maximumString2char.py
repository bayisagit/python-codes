from collections import Counter

class Solution:
    def lons(self,word:str, k:int) -> int:
        words=Counter()
        left=0
        m=len(word)
        be=0
        for right in range(m):
            words[word[right]]+=1
            while len(words)>k:
                words[word[left]] -=1
                if words[word[left]]==0:
                    del words[word[left]]
                left+=1
            be=max(be,right-left+1)
        return be
word=input("word: ")
n=int(input("possible character: "))
solution=Solution()
can=solution.lons(word,n)
print(can)