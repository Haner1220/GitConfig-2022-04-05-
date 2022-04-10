import itertools
a,b=map(int,input().split())
arr=[*map(int,input().split())]
rst=[]
combi=[]
for i in range(1,len(arr)+1):
    x=itertools.combinations(arr, i)
    combi.append(list(x))
for i in combi:
    for j in i:
        rst.append(sum(j))
print(rst.count(b))


