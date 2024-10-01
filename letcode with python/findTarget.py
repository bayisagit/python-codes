def nums(com):
    target=9
    for i in range(len(com)):
        for j in range(i+1,len(com)):
            if com[i]+com[j]==target:
                return [i,j]
com=[2,5,3,6]
ret=nums(com)
print(ret)
            
            