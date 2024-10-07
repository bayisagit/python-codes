m,n = map(int,input().split())
arr=list(map(int,input().split()))
l,cs,ts = 0,0,0
for i in range(m):
    cs+=arr[i]
    while cs>n:
        cs -= arr[l]
        l+=1
    ts=max(ts,i-l+1)
print(ts)