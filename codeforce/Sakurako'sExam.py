def can_balance(t, cases):
    results = []
    for a, b in cases:
        total_sum = a + 2 * b
        if total_sum % 2 != 0:
            results.append("NO")
        else:
            half_sum = total_sum // 2
            
            max_twos = min(b, half_sum // 2)
            remaining = half_sum - max_twos * 2
            
            if remaining <= a and remaining >= 0:
                results.append("YES")
            else:
                results.append("NO")
    return results

# Example usage
t = int(input())  # Input the number of test cases
cases = [tuple(map(int, input().split())) for _ in range(t)]  # Input each case as a tuple
outputs = can_balance(t, cases)
for result in outputs:
    print(result)