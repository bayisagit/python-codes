def yasser_happy(t, test_cases):
    results = []

    for n, a in test_cases:
        total = sum(a)

        prefix_sum = 0
        is_unhappy = False
        for i in range(n - 1):
            prefix_sum += a[i]
            if prefix_sum >= total:
                is_unhappy = True
                break

        if not is_unhappy:
            suffix_sum = 0
            for i in range(n - 1, 0, -1):
                suffix_sum += a[i]
                if suffix_sum >= total:
                    is_unhappy = True
                    break

        results.append("NO" if is_unhappy else "YES")

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

for res in yasser_happy(t, test_cases):
    print(res)
