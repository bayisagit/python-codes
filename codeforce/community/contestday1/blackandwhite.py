t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    # Count W's in the first window of size k
    current_w = s[:k].count('W')
    min_w = current_w

    # Slide the window
    for i in range(k, n):
        if s[i - k] == 'W':
            current_w -= 1
        if s[i] == 'W':
            current_w += 1
        min_w = min(min_w, current_w)

    print(min_w)
