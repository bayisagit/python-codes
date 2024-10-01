nums=input("enter the numbers")
nums=[int(x) for x in nums.split()]
nums.sort()
def fin(nums):
    for i in range(len(nums)):
        if nums[i]!=i:
            return i
    return len(nums)
result=fin(nums)
print(f"the missed number is {result}")