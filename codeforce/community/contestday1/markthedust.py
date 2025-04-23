t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_operations = 0
    found_non_zero = False
    
    for i in range(n - 1):  # exclude the last room
        if a[i] != 0:
            total_operations += a[i]
            found_non_zero = True
        elif found_non_zero:
            total_operations += 1  # need to skip this zero to reach next dust
    
    print(total_operations)
