def sort(nums):
    for i in range(len(nums)-1):
        minpose=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[i]:
                minpose=j
        nums[i],nums[minpose]=nums[minpose],nums[i]

nums=[5,3,8,6,7,2]
sort(nums)
print(nums)