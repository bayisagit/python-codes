def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        weights = list(map(int, input().split()))

        left, right = 0, n - 1
        alice_sum, bob_sum = 0, 0
        total_candies = 0

        while left <= right:
            if alice_sum < bob_sum:
                alice_sum += weights[left]
                left += 1
            elif bob_sum < alice_sum:
                bob_sum += weights[right]
                right -= 1
            else:
                total_candies = max(total_candies, left + (n - 1 - right) + 1)
                alice_sum += weights[left]
                bob_sum += weights[right]
                left += 1
                right -= 1
        
        total_candies = max(total_candies, left + (n - 1 - right))
        print(total_candies)

solve()
