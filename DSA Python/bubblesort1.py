def bay(nums):
    r=len(nums)
    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    return nums
    

nums=[8,4,5,2,0,5,4]
nu=bay(nums)
print(nu)