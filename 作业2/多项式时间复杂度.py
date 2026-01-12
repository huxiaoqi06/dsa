l=input().split('+')
m=0
for i in range(len(l)):
    li=len(l[i])
    for j in range(li):
        if l[i][j]=='n':
            if j==0:
                a=1
            else:
                a=int(l[i][:j])
            b=int(l[i][j+2:])
    if a!=0 and b>m:
        m=b
print('n^'+str(m))
