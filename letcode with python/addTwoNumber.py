l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l="".join(map(str,reversed(l1)))
ll="".join(map(str,reversed(l2)))
ts=str(int(l)+int(ll))
s=list(map(int,reversed(ts)))

print(s)
