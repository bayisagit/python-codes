def chocolate_bars(n, times):
    mieraf_time = 0
    naol_time = 0
    mieraf_bars = 0
    naol_bars = 0
    left = 0
    right = n - 1
    
    while left <= right:
        if mieraf_time <= naol_time:
            mieraf_time += times[left]
            mieraf_bars += 1
            left += 1
        else:
            naol_time += times[right]
            naol_bars += 1
            right -= 1
            
    return mieraf_bars, naol_bars

# Input reading
n = int(input())
times = list(map(int, input().split()))

# Get the result
result = chocolate_bars(n, times)

# Output the result
print(result[0], result[1])
