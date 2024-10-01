import math

def can_form_square(t, cases):
    results = []
    for n, s in cases:
        # Check if n is a perfect square
        k = int(math.isqrt(n))
        if k * k != n:
            results.append("No")
            continue
        
        # Check if the first and last rows are all '1's
        first_row = s[:k]
        last_row = s[-k:]
        if first_row != '1' * k or last_row != '1' * k:
            results.append("No")
            continue

        # Check the first and last column for every row
        valid = True
        for i in range(k):
            # Each row starts at index i*k and ends at index i*k + (k - 1)
            if s[i * k] != '1' or s[i * k + (k - 1)] != '1':
                valid = False
                break

        # If we have inner rows, check them too
        for i in range(1, k - 1):
            if s[i * k] != '1' or s[i * k + (k - 1)] != '1':
                valid = False
                break
            
            # Ensure that the inner elements are either '1' or '0'
            for j in range(1, k - 1):
                if s[i * k + j] != '0':
                    valid = False
                    break

        results.append("Yes" if valid else "No")
    
    return results

# Example usage
t = int(input())  # Number of test cases
cases = [(int(input()), input().strip()) for _ in range(t)]  # (n, s) pairs
outputs = can_form_square(t, cases)
for result in outputs:
    print(result)