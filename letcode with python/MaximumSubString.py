def bays(nums,k):
    left,curr,ans=0,0,0
    for right in range(len(nums)):
        curr+=nums[right]
        while curr>k:
            curr-=nums[left]
            left+=1
        ans=max(ans,right-left+1)
    return ans
    
nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
com=bays(nums,k)
print(com)