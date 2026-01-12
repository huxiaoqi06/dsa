n,k=map(int,input().strip().split())
l=[]
for _ in range(n):
    l.append(int(input().strip()))
i=1
j=max(l)
while i<=j:
    m=(i+j)//2
    num=0
    for a in l:
        num+=a//m
    if num>=k:
        ans=m
        i=m+1
    else:
        j=m-1
if sum(l)<k:
    print(0)
else:
    print(ans)