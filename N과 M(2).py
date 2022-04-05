import itertools
a,b=map(int,input().split())
arr=list(map(str,range(1,a+1)))

for i in itertools.permutations(arr,b):  #permutation : 모든 경우의 순열을 반대정렬값 포함 나열
    
    sorted_number = tuple(sorted(i, key=lambda x: int(x)))     #lambda=익명함수 튜플을 정렬해줌
    
    if i==sorted_number:                                       #i가 오름차순 정렬된 값과 일치할 시 출력
        for j in range(b):
            print(i[j],'',end='')
        print('\n',end='')
    