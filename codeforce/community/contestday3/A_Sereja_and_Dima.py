n=int(input(""))
nums = list(map(int, input().split()))
l=0
r=n-1
sereja=0
dima=0
for i in range(n):
    if i % 2 == 0:
        if nums[l] >= nums[r]:
            sereja += nums[l]
            l += 1
        else:
            sereja += nums[r]
            r -= 1
    else:
        if nums[l] >= nums[r]:
            dima += nums[l]
            l += 1
        else:
            dima += nums[r]
            r -= 1
print (f"{sereja} {dima}")