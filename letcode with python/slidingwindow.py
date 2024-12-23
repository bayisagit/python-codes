def max_sum_subarray(arr, k):
    max_sum=float("-inf")
    window_sum=0

    for start in range(len(arr)-k):
        window_sum = sum(arr[start:start+k])  # Add the next element
        max_sum=max(max_sum,window_sum)
    return max_sum

# Example usage
array = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(array, k))  # Output: 9 (5 + 1 + 3)
