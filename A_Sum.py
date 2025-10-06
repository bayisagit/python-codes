def yesorno(nums:list) ->str:
    fsum=sum(nums)
    for i in nums:
        if fsum-i == i:
            return "YES"
    return "NO"
n=int(input())
for _ in range(n):
    nums=[int(x) for x in input().split()]
    res=yesorno(nums)
    print(res)