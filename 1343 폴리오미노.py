a=input()
if a.count('X')+a.count('.')!=len(a):
    print(-1)
elif a.count('X')==0:
    print(a)
else:
    a=a.replace('XXXX','AAAA')  #XXXX=AAAA
    a=a.replace('XX','BB')      #XX=BB
    if a.count('X')>0:      #X가 남아있으면 -1 출력 
        print(-1)
    else:                       #X가 없으면 a출력
        print(a)
