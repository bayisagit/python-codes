n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# Create an array to hold the merged result
merged = []
i, j = 0, 0

# Merge the two arrays
while i < n and j < m:
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

# If there are remaining elements in array a
while i < n:
    merged.append(a[i])
    i += 1

# If there are remaining elements in array b
while j < m:
    merged.append(b[j])
    j += 1

# Print the merged array
print(" ".join(map(str, merged)))