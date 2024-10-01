n=int(input())
newstud=[]
for _ in range(n):       
    name = input()
    score = float(input())
    newstud.append([name,score])
newstud.sort(key=lambda x:x[1])
se=None
for i in range(1,n):
    if newstud[i][1]!= newstud[0][1]:
        se=newstud[i][1]
        break
secon=[student[0] for student in newstud if student[1]==se]
secon.sort()
for name in secon:
    print(name)