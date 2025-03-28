def cal(inp:list)->int:
    onescn=inp.count(1)
    wincn=sum(inp[:onescn])
    mxwin=wincn
    for i in range(onescn,len(inp)):
        wincn+=inp[i]
        wincn-=inp[i-onescn]
        mxwin=max(mxwin,wincn)
    return onescn-mxwin
        
        
inp=list(map(int,input("enter the bits: ").split()))
val=cal(inp)
print(val)
