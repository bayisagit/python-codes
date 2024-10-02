t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    rob = 0
    cnt = 0
    for num in arr:
        if num >= k:
            rob += num
        if num == 0 and rob > 0:
            cnt += 1
            rob -= 1
    print(cnt)