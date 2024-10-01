def bays(firsel,nesel):
    nums=[]
    for k in range(len(nesel)):
        count=0
        for j in range(len(firsel)):
            if firsel[j]<nesel[k]:
                count+=1
        nums.append(count)
    return nums

fi=int(input("enter how many elements for the first array: "))
ne=int(input("enter how many elements for the last array: "))
print("enter the numbers in ascending order")
firsel=[]
for i in range(fi):
    firsel.append(int(input(f"enter the the {i+1} element")))
nesel=[]
for i in range(ne):
    nesel.append(int(input(f"enter the the {i+1} element")))
    
resu=bays(firsel,nesel)
print(resu)
    

