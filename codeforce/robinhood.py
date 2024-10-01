def will_have_even_leaves(t, test_cases):
    results = []
    
    for n, k in test_cases:
        # Calculate total leaves using the sum formula
        total_leaves = (n * (n + 1)) // 2 - ((n - k) * (n - k + 1)) // 2
        
        # Check if total leaves is even
        if total_leaves % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read the number of test cases
t = int(input().strip())
test_cases = []

# Read each test case
for _ in range(t):
    n, k = map(int, input().strip().split())
    test_cases.append((n, k))

# Get results and print them
results = will_have_even_leaves(t, test_cases)
for res in results:
    print(res)