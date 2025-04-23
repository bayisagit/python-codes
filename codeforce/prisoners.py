def count_valid_segments(n, t, c, severities):
    count = 0
    valid_length = 0
    
    # Traverse the severity list
    for i in range(n):
        if severities[i] <= t:
            valid_length += 1
        else:
            valid_length = 0
        
        # If we have a valid segment of length >= c, count it
        if valid_length >= c:
            count += 1
    
    return count

# Input reading
n, t, c = map(int, input().split())
severities = list(map(int, input().split()))

# Get the result
result = count_valid_segments(n, t, c, severities)

# Output the result
print(result)
