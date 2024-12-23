def bay(nums,keys):
    r=len(nums)
    for i in range(r):
        if keys == nums[i]:
            return True
    return False

    

nums=[8,4,5,2,0,5,4]
keys=5
nu=bay(nums,keys)
print(nu)