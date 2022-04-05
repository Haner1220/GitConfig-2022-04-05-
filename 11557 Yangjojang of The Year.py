a=int(input())
cml=[]
mList=[]
for i in range(a):
    b=int(input())
    for i in range(b):
        m,n=[*map(str,input().split())]
        mList.append(m)
        cml.append(int(n))
    print(mList[cml.index(max(cml))])
