s = "iii"
myd={
    "i":1,
    "v":5,
    "x":10,
    "l":50,
    "c":100,
    "d":500,
    "m":100
}
sums=0
r=0
for k in reversed(s):
    curr=myd[k]
    if curr<r:
        sums -= curr
    else:
        sums += curr
    r=curr
print(sums)
    