def robin(k,testc):
    rek=[]
    for case in testc:
        n,m,gold=case
        robg=0
        robgi=0
        for g in gold:
            if g>=m:
                robg+=g
            elif g==0 and robg>0:
                robg-=1
                robgi+=1
        rek.append(robgi)
    return rek
        
k=int(input().strip())
testc=[]
for i in range(k):
    n, m=map(int,input().strip().split())
    gold=list(map(int,input().strip().split()))
    testc.append((n,m,gold))
results=robin(k,testc)
for res in results:
    print(res)
    
