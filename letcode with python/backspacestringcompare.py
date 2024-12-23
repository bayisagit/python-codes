def backspaceCompare(s: str, t: str) -> bool:
    sta=[]
    staa=[]
    for i in s:
        if i == '#':
            if sta:
                sta.pop()
        else:
            sta.append(i)
    for i in t:
        if i == '#':
            if staa:
                staa.pop()
        else:
            staa.append(i)
    return ''.join(sta) == ''.join(staa)
s=input("enter the strings")
t=input("enter the second string")
l=backspaceCompare(s,t)
print(l)