def f(l,n):
    s=0
    if n==0:
        return 0
    if n==1:
        return l[0][0]
    for i in range(n):
        s+=l[0][i]+l[-1][i]
    for i in range(1,n-1):
        s+=l[i][0]+l[i][-1]
    del l[-1]
    del l[0]
    for i in range(n-2):
        del l[i][0]
        del l[i][-1]
    return max(s,f(l,n-2))
n=int(input().strip())
l=[]
for _ in range(n):
    li=list(map(int,input().strip().split()))
    l.append(li)
print(f(l,n))