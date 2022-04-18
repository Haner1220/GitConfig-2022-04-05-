x=[]
for i in range(7):
    y=int(input())
    if y%2!=0:x.append(y) 
print(-1) if len(x)==0 else print(sum(x),min(x))

