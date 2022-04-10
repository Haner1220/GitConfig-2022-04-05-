a=str(input())
x=""
i=1
while True:
    x=x+str(i)
    if x.count(a)==True:
       print(x.index(a)+1)
       break
    i+=1
