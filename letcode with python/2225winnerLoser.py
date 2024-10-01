matches=input("enter the matches using space ")
matches=[int(x) for x in matches.split()]
matches=[[matches[i],matches[i+1]] for i in range(0,len(matches),2)]
def winerloser(matches):
    finalres=[[],[]]
    d={}
    for i in matches:
        d[i[1]] = d.get(i[1],0)+1
        d[i[0]] = d.get(i[0],0)+0
    for k,v in d.items():
        if v==0:
            finalres[0].append(k)
        elif v==1:
            finalres[1].append(k)
    finalres[0].sort()
    finalres[1].sort()
    return finalres
resl=winerloser(matches)
print(f"the winner and loser are {resl}")