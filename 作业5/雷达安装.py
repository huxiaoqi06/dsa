c=0
while True:
    c+=1
    n,d=map(int,input().strip().split())
    if n==0 and d==0:
        break
    l=[]
    judge=0
    for _ in range(n):
        x,y=map(int,input().strip().split())
        if y>d:
            judge=1
        dx=(d**2-y**2)**0.5
        l.append([x-dx,x+dx])

    if judge:
        print(f'Case {c}: -1')
        input()
        continue
    l.sort(key=lambda x:x[1])
    p=l[0][1]
    count=1
    for i in range(1,n):
        if l[i][0]>p:
            p=l[i][1]
            count+=1
    print(f'Case {c}: {count}')
    input()
