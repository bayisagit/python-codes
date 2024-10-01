def max_good_array_length(t, cases):
    results = []
    for l, r in cases:
        max_length = 0
        diff = r - l
        
        # We need to find the largest i such that (i-1)*i/2 <= diff
        while (max_length * (max_length + 1)) // 2 <= diff:
            max_length += 1
        
        results.append(max_length)
    
    return results

# Example usage
t = int(input())  # Number of test cases
cases = [tuple(map(int, input().strip().split())) for _ in range(t)]  # (l, r) pairs
outputs = max_good_array_length(t, cases)
for result in outputs:
    print(result)