import itertools
a,b=map(int,input().split())
arr=list(map(str,range(1,a+1)))

for i in itertools.permutations(arr,b):
    for j in range(b):
        print(i[j],'',end='')
    print('\n',end='')
    