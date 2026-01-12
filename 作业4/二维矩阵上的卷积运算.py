m,n,p,q=map(int,input().strip().split())
l1=[]
for i in range(m):
    l1.append(list(map(int,input().strip().split())))

l2=[]
for i in range(p):
    l2.append(list(map(int,input().strip().split())))    

for i in range(m+1-p):
    s=[]
    for j in range(n+1-q):
        aij=0
        for k in range(i,i+p):
            for l in range(j,j+q):
                aij+=l1[k][l]*l2[k-i][l-j]
        s.append(aij)
    print(*s)