a=int(input())
b=int(input())

cnt=0
graph = [[]*a for _ in range(a+1)]
visited=[0]*(a+1)
for i in range(b):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(start):
    global cnt
    visited[start]=True
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt+=1
dfs(1)
print(cnt)