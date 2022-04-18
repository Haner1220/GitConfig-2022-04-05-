a,b=map(int,input().split())
c=list(range(a,b+1))
c=list(map(str,c))
first=[]
sec=[]
for i in c:
    i=i.replace("1","one")
    i=i.replace("2","two")
    i=i.replace("3","three")
    i=i.replace("4","four")
    i=i.replace("5","five")
    i=i.replace("6","six")
    i=i.replace("7","seven")
    i=i.replace("8","eight")
    i=i.replace("9","nine")
    i=i.replace("0","zero")
    first.append(i)
first.sort()
cnt=0
for i in first:
    i=i.replace("one","1")
    i=i.replace("two","2")
    i=i.replace("three","3")
    i=i.replace("four","4")
    i=i.replace("five","5")
    i=i.replace("six","6")
    i=i.replace("seven","7")
    i=i.replace("eight","8")
    i=i.replace("nine","9")
    i=i.replace("zero","0")
    print(i,end=' ')
    cnt+=1
    if cnt%10==0:
        print()

    
    