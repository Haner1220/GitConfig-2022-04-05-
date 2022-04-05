from itertools import product
a,b=map(int,input().split())
arr=list(map(str,range(1,a+1)))

for i in product(arr,repeat=b):  #arr 순열할 리스트, repeat=만들 리스트 길이 제한
    for j in range(b):
        print(i[j],'',end='')
    print('\n',end='')
    