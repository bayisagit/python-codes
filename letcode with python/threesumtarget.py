def calc(nums:list,ta:int)->int:
    nums.sort()
    l=len(nums)
    ans=0
    for i in range(l):
        j=i+1
        k=l-1
        while j<k:
            sum=nums[i]+nums[j]+nums[k]
            if sum<ta:
                ans+=k-j
                j+=1
            else:
                k-=1
    return ans

nums=list(map(int,input("enter the numbers using spaces: ").split()))
ta=int(input("enter the target number: "))
d=calc(nums,ta)
print(d)