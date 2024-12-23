def val(s:str)->str:
    result=[]
    for i in s:
        if i != "*":
            result.append(i)
        else:
            if result:
                result.pop()
    return ''.join(result)
s=input("enter the string")
l=val(s)
print(l)