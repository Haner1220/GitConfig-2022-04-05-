def gop(a):
    sum=1
    N=[int(i) for i in str(a)] 
    for i in N:
        sum*=i
    return sum

a=str(input())
z=1
rst="NO"
LA=len(a)

for i in range(LA-1):
    if gop(a[0:z]) == gop(a[z:LA]):
        rst="YES"
        break
    z+=1
    
print(rst)
    

