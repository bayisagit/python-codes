n, m = map(int,input().split())
firs=list(map(int,input().split()))
seco=list(map(int,input().split()))
g=[]
cnt = 0
l, r = 0, 0
while  r < m:
    while l<n  and firs[l] < seco[r]:
        cnt += 1
        l += 1
    r += 1
    g.append(cnt)
print(*g)
        
    