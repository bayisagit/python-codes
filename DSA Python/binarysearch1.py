def bay(nums,keys):
    l,r=0,len(nums)
    while l<r:
       mid=(l+r)//2
       if nums[mid] == keys:
           return mid
       elif nums[mid] < keys:
           l=mid + 1
       elif nums[mid] > keys:
           r=mid
    return -1
nums=[2,3,4,5,6,7,8]
keys = 9
nu=bay(nums,keys)
print(nu)

