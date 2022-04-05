a=[]
a=[*map(str,input())]
cnt=[]
aCnt=0
spsCnt=0
for i in range(0,11):
    aCnt==a.count(str(i))
    if i == 6 or i==9:
        spsCnt+=a.count(str(i))
    else:
        cnt.append(a.count(str(i)))
cnt.append(spsCnt//2+spsCnt%2)
print(max(cnt))