def bayo(nums,k):
    k=k%len(nums)
    u=len(nums)-k
    now=nums[0:u]
    nums[0:u]=[]
    nums.extend(now)
    return nums
    
    
nums = [1,2,3,4,5,6,7]
k = 3
kw=bayo(nums,k)
print(kw)