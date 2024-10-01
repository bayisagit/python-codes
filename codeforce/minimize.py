# Read the number of test cases
t = int(input())

# Initialize a list to store results
results = []

# Process each test case
for _ in range(t):
    a, b = map(int, input().split())
    result = b - a
    results.append(result)

# Print all results at once
print("\n".join(map(str, results)))