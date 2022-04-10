a=int(input())
for _ in range(a):
    cnt=0
    b,c=map(int,input().split())
    for i in range(b,c+1):
        if str(i).count('0')>0:
            cnt+=str(i).count('0')
    print(cnt)