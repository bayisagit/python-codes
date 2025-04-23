t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_so_far = a[-1]
    bad_days = 0

    for i in range(n - 2, -1, -1):
        if a[i] > min_so_far:
            bad_days += 1
        else:
            min_so_far = a[i]

    print(bad_days)
