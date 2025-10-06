# list1 = [1, 2, 8]
n,m = map(int,input().split())
list1 = list(map(int,input().split()))
list1.sort()
# list2 = [4, 0, 6]
list2=list(map(int,input().split()))
list2.append(5)
list2.sort()

# list3 = list1 + list2
# sortedlist = sorted(list3)
# print(sortedlist)

l,r = 0,0
newarray = []

while l < n and r < m:
    if list1[l] <= list2[r]:
        newarray.append(list1[l])
        l += 1
    else:
        newarray.append(list2[r])
        r += 1
while l < n:
    newarray.append(list1[l])
    l += 1
while r < m:
    newarray.append(list2[r])
    r += 1
print(newarray)
