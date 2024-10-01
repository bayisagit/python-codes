s=input("enter the string you want ")
newst=""
for k in s:
    if k.isupper():
        newst+=k.lower()
    elif k.islower():
        newst+=k.upper()
    else:
        newst+=k
print(newst)