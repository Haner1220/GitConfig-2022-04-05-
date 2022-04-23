a,b=map(int,input().split())
print(max([int(str(a*i)[::-1])for i in range(1,b+1)]))
