# def sum_alternating(arr):
#     total = 0
#     i = 0
#     n = len(arr)
    
#     while i < n:
#         current = arr[i]
        
#         while i + 1 < n and (arr[i + 1] * current > 0):
#             i += 1
#             current = max(current, arr[i])
        
#         total += current
#         i += 1
    
#     return total

# t = int(input(""))
# for _ in range(t):
#     n = int(input(""))
#     arr = list(map(int, input("").split()))
#     print(sum_alternating(arr))
m, n = 3, 4
result = [[0] * n for _ in range(m)]
print(result) 