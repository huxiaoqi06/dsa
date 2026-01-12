row1,col1=map(int,input().split())
A=[]
for i in range(row1):
    A.append(list(map(int,input().split())))
row2,col2=map(int,input().split())
B=[]
for i in range(row2):
    B.append(list(map(int,input().split())))
row3,col3=map(int,input().split())
C=[]
for i in range(row3):
    C.append(list(map(int,input().split())))
if col1!=row2 or row1!=row3 or col2!=col3:
    print("Error!")
else:
    for i in range(row3):
        l=[]
        for j in range(col3):
            ij=C[i][j]
            for k in range(col1):
                ij+=A[i][k]*B[k][j]
            l.append(ij)
        print(*l)