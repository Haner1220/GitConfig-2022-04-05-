a=int(input())
for i in range(a):
    x=map(int,input().split())
    N=[i for i in x if i%2==0]
    print(sum(N),min(N))