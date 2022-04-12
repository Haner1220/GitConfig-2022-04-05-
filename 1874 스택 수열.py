for i in range(int(input())):
    c=0
    a=input()
    stack=[]
    for j in a:
        if j=="(":
            stack.append(j)
        elif j==")":
            if len(stack) == 0:
                print("NO")
                c=1
                break
            else:
                stack.pop()
    if c!=1:
        if len(stack)==0:
            print("YES")
        else:
            print("NO")
