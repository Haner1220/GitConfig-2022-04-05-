a=int(input())
ply=[]
rst=[]
for i in range(a):
    x=input()[:1]
    ply.append(x)
setPly=set(ply)
for i in setPly:
    if ply.count(i)>=5:
        rst.append(i)

if len(rst)==0:
    print("PREDAJA")

else:
    rst.sort()
    print("".join(rst))