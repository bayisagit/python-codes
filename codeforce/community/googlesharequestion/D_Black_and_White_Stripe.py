def min_recolorings(t, test_cases):
    results = []

    for n, k, s in test_cases:
        count_white = s[:k].count('W')
        min_white = count_white

        for i in range(k, n):
            if s[i - k] == 'W':
                count_white -= 1
            if s[i] == 'W':
                count_white += 1
            min_white = min(min_white, count_white)

        results.append(min_white)

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    test_cases.append((n, k, s))

for res in min_recolorings(t, test_cases):
    print(res)
