rst=[]
import sys
from collections import deque
input=sys.stdin.readline
a=int(input())
stack=0
for _ in range(a):
  fnc=list(input())
  g=int(input())
  queue = deque(input().strip('[\n]').split(','))
  x=len(queue)
 
  for i in fnc:
    if g<fnc.count('D') or len(deque)==0 and i=='D':
        rst.append('error')
        break 
    if i=='R':
       stack+=1
    elif i=='D':
        
        if stack%2==0:
            queue.popleft()
        elif stack%2!=0:
            queue.pop()
  if stack%2!=0:
      queue.reverse()
  if len(rst)>0:
        print("\n".join(rst),sep='')
  elif len(queue)>=0:
      print('[',",".join(queue),']',sep='')
  
  rst.clear()
  stack=0

  
  
