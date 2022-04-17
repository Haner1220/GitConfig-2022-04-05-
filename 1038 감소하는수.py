from itertools import combinations

a=int(input())
rst1=[]
for i in range(1,11):
    for j in combinations(range(0,10),i):
        j=list(j)
        j.sort(reverse=True)
        rst1.append(int("".join(list(map(str,j)))))
rst1.sort()
try:
    print(rst1[a])
except:
    print(-1)