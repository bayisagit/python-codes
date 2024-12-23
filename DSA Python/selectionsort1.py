def bay(nums):
    r=len(nums)
    for i in range(r-1):
        u=i
        for j in range(i+1,r):
            if nums[j]<nums[u]:
                u=j
        if u != i:
            temp=nums[i]
            nums[i]=nums[u]
            nums[u]=temp
    return nums
    

nums=[8,4,5,2,0,5,4]
nu=bay(nums)
print(nu)