list1 = list(map(int,input().split()))
list1.sort()
target = 25
l,r = 0,len(list1)-1
while l < r:
    current_sum = list1[l] + list1[r]
    if current_sum == target:
        print(f"Pair found on Index: ({l}, {r})")
        break
    elif current_sum < target:
        l += 1
    else:
        r -= 1
        