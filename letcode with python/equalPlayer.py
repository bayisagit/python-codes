def bays(skill):
    du=0
    k=sum(skill)
    if len(skill)==2:
        return skill[0]*skill[1]
    if len(skill)%2==0 and k%(len(skill)/2)==0:
        ratio=k//(len(skill)//2)
    else:
        return -1
    skill.sort()
    for i in range(len(skill)//2):
        if skill[i]+skill[len(skill)-(i+1)]!= ratio:
            return -1
        du+=skill[i]*skill[len(skill)-(i+1)]
    return du
skill = [3,2,5,1,3,4]
re=bays(skill)
print(re)