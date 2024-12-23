def bay(nums):
    r=len(nums)
    for i in range(r):
        for j in range(i,0,-1):
            if nums[j-1]>nums[j]:
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
    return nums
    

nums=[8,4,5,2,0,5,4]
nu=bay(nums)
print(nu)