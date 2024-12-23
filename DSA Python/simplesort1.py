def bay(nums):
    r=len(nums)
    for i in range(r-1):
        for j in range(i+1,r):
            if nums[j]<nums[i]:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
    return nums
    

nums=[8,4,5,2,0,5,4]
nu=bay(nums)
print(nu)