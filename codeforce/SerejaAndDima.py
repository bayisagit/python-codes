def bays(n,arr):
    sereja=0
    dima=0
    left=0
    right=n-1
    for i in range(n):
        if arr[left]>arr[right]:
            curr=arr[left]
            left+=1
        else:
            curr=arr[right]
            right-=1
        if i%2:
            dima+=curr
        else:
            sereja+=curr
    return (sereja,dima)
n=int(input())
arr=list(map(int,input().split()))
com=bays(n,arr)
print(com[0],com[1])
        
    
