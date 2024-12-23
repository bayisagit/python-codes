def sol(nums:list, k:int)->int:
    nums.sort()
    mxn=-1
    l,r=0,len(nums)-1
    while l<r:
        mxs=nums[r]+nums[l]
        if mxs<k:
            mxn=max(mxn,mxs)
            l+=1
        else:
            r-=1
    return mxn
    


h=input("enter how many numbers woul you want enter: ")
k=input("enter the target element: ")
nums=[map(int,input(f"enter {h} numbers separated by space").split())]
ans=sol(nums,k)
print(ans)
    