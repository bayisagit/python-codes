def min_coins_to_make_unique(n, badges):
    badges.sort()
    coins = 0
    for i in range(1, n):
        if badges[i] <= badges[i - 1]:
            coins += badges[i - 1] - badges[i] + 1
            badges[i] = badges[i - 1] + 1
    return coins

# Input reading
n = int(input())
badges = list(map(int, input().split()))

# Get the result
result = min_coins_to_make_unique(n, badges)

# Output the result
print(result)
