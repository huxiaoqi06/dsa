n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input().strip()))
i=max(l)
j=sum(l)
while i<=j:
    d=(i+j)//2
    num=1
    s=0
    for k in range(n):
        if s+l[k]>d:
            s=l[k]
            num+=1
        else:
            s+=l[k]
    if num<=m:
        ans=d
        j=d-1
    else:
        i=d+1
print(ans)
