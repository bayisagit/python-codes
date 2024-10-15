s = "abcabcbb"
st=""
ms=0
left=0
right=1
for i in range(len(s)):
    if s[i] in st:
        st = st[1:]
        left += 1
    st += s[i]
    ms=max(ms,i-left+1)
print(ms)