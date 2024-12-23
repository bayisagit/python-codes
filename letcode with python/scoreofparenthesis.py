def val(s:str)->int:
    sta=[]
    score=0
    for i in s:
        if i == '(':
            sta.append(score)
            score=0
        else:
            score=sta.pop()+max(2*score,1)
    return score
s=input("enter your paranthesis:")
k=val(s)
print(k)
