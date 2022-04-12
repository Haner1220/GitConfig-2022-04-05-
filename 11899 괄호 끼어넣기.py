a=input()
cnt=0
stack=[]
for i in a:
    if i=="(":
        stack.append(i)
    elif i==")" and len(stack)>0:   # 닫는 괄호가 있고 stack에 여는 괄호가 하나라도 있으면 stack.pop
        stack.pop()
    else:
        cnt+=1                  #아니라면 cnt+=1
print(cnt+len(stack))