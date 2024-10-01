mat=[[0,  1,  2,  3],
 [4,  5,  6,  7],       
 [8,  9,  10, 11]]  
flatten=[]
newmat=[]
r=2
c=6
for k in mat:
    for k in k:
        flatten.append(k)
print(flatten)
for d in range(r-1):
    newmat.append(flatten[d*c : d*c + c])
print(newmat)
    