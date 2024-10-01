def bays(s, subs):
    subsc = 0
    d = 0
    subscc = 0
    k = 0
    
    for i in range(len(s)):
        if d < len(subs) and subs[d] == s[i]:
            d += 1
            subsc += 1
            
            if subsc == len(subs):
                subscc += 1
                subsc = 0
                d = 0
        else:
            if d > 0:  # Reset only if we had started matching
                i -= d  # Move back to check for the next potential match
                d = 0
                subsc = 0
            
    return subscc

s = input()
n = int(input())
substring = [input() for i in range(n)]
for subs in substring:
    com = bays(s, subs)
    print(com)