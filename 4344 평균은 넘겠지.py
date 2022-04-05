a=int(input())
b=[]
c=[]
cnt=0
for _ in range(a):
    b=list(map(int,input().split()))
    c=b[1:]
    for i in c:
        if i>sum(b[1:])/b[0]:
            cnt+=1
    print(f"{cnt/b[0]*100:.3f}",'%',sep='')
    cnt=0

