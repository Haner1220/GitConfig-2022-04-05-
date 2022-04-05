rst=[]
import sys
from collections import deque
input=sys.stdin.readline
a=int(input())
stack=0
for _ in range(a):
    fnc=list(input())
    num=int(input())
    queue = deque(input().strip('[\n]').split(','))
    for i in fnc:
        if i=='R':
            stack+=1
        elif i=='D':
            if stack%2==0:
                if len(queue)==0:
                    break
                else:
                    queue.popleft()
            else:
                if len(queue)==0:
                    break
                else:
                    queue.pop()
    
    if stack%2!=0:
        queue.reverse()
    stack=0
    if fnc.count('D')>num:
        print('error')
    elif len(queue)==0:
        print('[]')
    else:
        print('[',",".join(queue),']',sep='')
    