n=int(input())
l=[]
for i in range(n):
    name,q=map(str,input().split('-'))
    l.append([name,float(q[:-1]),q[:-1],q[-1]])
l.sort(key=lambda x: x[1])
l.sort(key=lambda x: x[3],reverse=True)
l.sort(key=lambda x: x[0])
for i in range(len(l)):
    if i==0:
        print(l[i][0]+": "+l[i][2]+l[i][3],end='')
    elif l[i-1][0]!=l[i][0]:
        print()
        print(l[i][0]+": "+l[i][2]+l[i][3],end='')
    else:
        print(', '+l[i][2]+l[i][3],end='')
