def bayo(s,sub):
    start=0
    count=0
    while True:
        start=s.find(sub,start)
        if start==-1:
            break
        count+=1
        start+=1
    return count
s=input()
n=int(input())
subst=[input() for i in range(n)]
for  sub in subst:
    com=bayo(s,sub)
    print(com)
    