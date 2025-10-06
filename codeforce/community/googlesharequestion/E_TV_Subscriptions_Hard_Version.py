from collections import defaultdict

def min_subscriptions(t, test_cases):
    results = []
    for n, k, d, a in test_cases:
        freq = defaultdict(int)
        unique = 0

        for i in range(d):
            if freq[a[i]] == 0:
                unique += 1
            freq[a[i]] += 1
        min_unique = unique

        for i in range(d, n):
            left = a[i - d]
            freq[left] -= 1
            if freq[left] == 0:
                unique -= 1

            right = a[i]
            if freq[right] == 0:
                unique += 1
            freq[right] += 1

            min_unique = min(min_unique, unique)

        results.append(min_unique)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, k, d, a))

for ans in min_subscriptions(t, test_cases):
    print(ans)
