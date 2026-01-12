n=int(input())
for _ in range(n):
    l=list(input().strip().split())
    stack=[]
    for c in l:
        if c=='/':
            b=stack.pop()
            a=stack.pop()
            num=a/b
            stack.append(num)
        elif c=='+':
            num=stack.pop()+stack.pop()
            stack.append(num)
        elif c=='-':
            num=-stack.pop()+stack.pop()
            stack.append(num)
        elif c=='*':
            num=stack.pop()*stack.pop()
            stack.append(num)
        else:
            stack.append(float(c))
    print(f'{stack[0]:.2f}')
