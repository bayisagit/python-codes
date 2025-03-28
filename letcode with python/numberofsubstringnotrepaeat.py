def calc(inpu:list,n:int)->int:
    cn=0
    for i in range(len(inpu)-n+1):
        vas=set(inp[i:n+i])
        if len(vas)== n:
            cn+=1
    return cn
        
inp=input("enter the string: ")
inpu=list(inp)
n=int(input("enter the number of substring: "))
cal=calc(inpu,n)
print(cal)