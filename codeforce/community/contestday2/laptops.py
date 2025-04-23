n = int(input())
laptops = []

for _ in range(n):
    a, b = map(int, input().split())
    laptops.append((a, b))

# Sort laptops by price
laptops.sort()

alex_is_happy = False

for i in range(n - 1):
    if laptops[i][1] > laptops[i + 1][1]:
        alex_is_happy = True
        break

if alex_is_happy:
    print("Happy Alex")
else:
    print("Poor Alex")
