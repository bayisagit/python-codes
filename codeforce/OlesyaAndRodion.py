def helper(n, t):
    if t == 10:
        if n == 1:
            return -1
        else:
            return int("1" + "0" * (n - 1))
    else:
        return int(str(t) * n)
n, t = map(int, input().split())
print(helper(n, t))