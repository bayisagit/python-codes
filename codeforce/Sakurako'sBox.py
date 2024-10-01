def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)

def expected_product(t, cases):
    MOD = 10**9 + 7
    results = []
    
    for n, a in cases:
        total_sum = sum(a) % MOD  # Sum of all elements
        P = (total_sum * total_sum) % MOD  # P = (sum(a))^2
        Q = (n * n) % MOD  # Q = n^2
        
        # Calculate P * Q^-1
        Q_inverse = mod_inverse(Q, MOD)
        result = (P * Q_inverse) % MOD
        
        results.append(result)
    
    return results

# Example usage
t = int(input())  # Number of test cases
cases = [(int(input()), list(map(int, input().strip().split()))) for _ in range(t)]  # (n, a) pairs
outputs = expected_product(t, cases)
for result in outputs:
    print(result)