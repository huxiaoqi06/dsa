n,c=map(int,input().split(' '))
l=[]
for i in range(n):
    l.append(int(input().strip()))
l.sort()
li=[]
for i in range(1,n):
    li.append(l[i]-l[i-1])
i=0
j=l[-1]-l[0]
while i<=j:
    d=(i+j)//2
    num=1
    s=0
    for k in range(n-1):
        s+=li[k]
        if s>=d:
            num+=1
            s=0
    if num>=c:
        ans=d
        i=d+1
    else:
        j=d-1
print(ans)