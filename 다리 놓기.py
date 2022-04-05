import math
a=int(input())

def factorial(maxE,minE): 
    if maxE-minE==0:
        return math.factorial(maxE)
    else:
        return math.factorial(maxE)//math.factorial(maxE-minE)
      
for i in range(a):
    b,c=list(map(int,input().split()))
    maxE=max(b,c)
    minE=min(b,c)
    print(factorial(maxE,minE) // math.factorial(minE))