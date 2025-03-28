def calc(nums: list) -> int:
    ts=sum(nums)
    ls=0
    for i in range(len(nums)):
        if (ts-ls) == ls:
            return i
        ls+=nums[i]
    return -1
nums = list(map(int, input("Enter the nums value: ").split()))
e = calc(nums)
print(e)