haystack = "leetcode"
needle = "leeto"
n=len(needle)
m=len(haystack)
for i in range(m-n+1):
    if haystack[i:n] == needle:
        print(i)
        break
    if i == m-n:
        print(-1)
