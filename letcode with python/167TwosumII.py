def bayo(numbers,target):
    le=0
    ri=len(numbers)-1
    while le<ri:
        cur=numbers[le]+numbers[ri]
        if cur==target:
            return [le,ri]
        elif cur<target:
            le+=1
        else:
            ri-=1
            
        

numbers=[2,7,11,15]
target=9

com=bayo(numbers,target)
print(com)
    