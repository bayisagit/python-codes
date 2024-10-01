s=input("enter the substring ")
t=input("enter the string ")
sp=0
tp=0
while sp<len(s):
    if s[sp] == t[tp]:
        sp+=1
    tp+=1
if sp == len(s):
    print("yes")
else:
    print("false")