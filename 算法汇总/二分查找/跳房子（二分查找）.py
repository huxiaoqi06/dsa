l,n,m=map(int,input().split(' '))
li=[]
for i in range(n):
    a=int(input().strip())
    li.append(a)
li.append(l)
for i in range(n,0,-1):
    li[i]-=li[i-1]
i=0
j=l
while i<=j:
    d=(i+j)//2
    num=0
    s=0
    for k in range(n+1):
        s+=li[k]
        if s<d:
            num+=1
        else:
            s=0
    if num<=m:
        ans=d
        i=d+1
    else:
        j=d-1
print(ans)