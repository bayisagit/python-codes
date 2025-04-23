s = input()
k = int(input())

if k > len(s):
    print("impossible")
else:
    # Count unique letters using a simple list
    seen = []
    for char in s:
        if char not in seen:
            seen.append(char)
    unique_letters = len(seen)
    
    if unique_letters >= k:
        print(0)
    else:
        print(k - unique_letters)
