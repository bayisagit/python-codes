def max_operations(n, s):
    s = list(s)
    operations = 0
    used = [False] * (n - 1)  # Track used indices
    
    while True:
        found_swap = False
        for i in range(n - 1):
            if not used[i] and s[i] == 'A' and s[i + 1] == 'B':
                s[i], s[i + 1] = s[i + 1], s[i]
                used[i] = True  # Mark index as used
                operations += 1
                found_swap = True
        if not found_swap:
            break
    
    return operations

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    print(max_operations(n, s))