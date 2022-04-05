a=int(input())

for _ in range(a):
  vo=0
  b,c,d=[*map(int,input().split())]
  dong=d%b
  if d%b==0:
      dong=b
  if d%b>0:
      vo=1
  print(dong,str(d//b+vo).rjust(2,"0"),sep='')
      