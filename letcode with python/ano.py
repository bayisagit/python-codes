ranges = [[1,10],[10,20]]
left = 21
right = 21
ranges.sort()
cn=0
for st,en in ranges:
    if st<=left and en>=left:
        cn+=1
    if st<=right and en>=right:
        cn+=1
if cn>1:
    print(True)
else:
    print(False)