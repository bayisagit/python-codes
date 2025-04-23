def can_transform(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return j == len(t)

n = int(input())
for _ in range(n):
    line = input().strip()
    if line:  # Check that the line is not empty
        s, t = line.split()
        if can_transform(s, t):
            print("YES")
        else:
            print("NO")
        