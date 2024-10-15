nums = [1,3,5,6]
target = 7
l,r = 0 , len(nums)-1
for i in range(1,len(nums)):
    if nums[i] == target:
        print(i)
        break
    elif nums[i] > target and nums[i-1] < target:
        print(i+1)
if nums[0] == target:
    print(0)
if nums[-1] < target:
    print(len(nums))
    
        
    