def count_inversions(arr):
    ones = 0
    inv = 0
    for x in arr:
        if x == 1:
            ones += 1
        else:
            inv += ones
    return inv

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Step 1: Original inversion
    base_inv = count_inversions(a)

    # Step 2: Try flipping first 0 to 1
    flip0 = a[:]
    for i in range(n):
        if flip0[i] == 0:
            flip0[i] = 1
            break
    inv_flip0 = count_inversions(flip0)

    # Step 3: Try flipping last 1 to 0
    flip1 = a[:]
    for i in range(n-1, -1, -1):
        if flip1[i] == 1:
            flip1[i] = 0
            break
    inv_flip1 = count_inversions(flip1)

    print(max(base_inv, inv_flip0, inv_flip1))
