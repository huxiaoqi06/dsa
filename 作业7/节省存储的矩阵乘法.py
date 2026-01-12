n,m1,m2=map(int,input().strip().split())
A=[]
B=[]
for _ in range(m1):
    A.append(list(map(int,input().strip().split())))
for _ in range(m2):
    B.append(list(map(int,input().strip().split())))
B.sort(key= lambda x:x[1])

r=c=0
C=[]

while r<n:
    Crc=0
    i=j=0
    while i<m1 and A[i][0]<r:
        i+=1
    while j<m2 and B[j][1]<c:
        j+=1
    while i<m1 and j<m2 and A[i][0]==r and B[j][1]==c:
        if B[j][0]>A[i][1]:
            i+=1
        elif B[j][0]==A[i][1]:
            Crc+=B[j][2]*A[i][2]
            i+=1
            j+=1
        else:
            j+=1
    if Crc:
        C.append([r,c,Crc])
    if c<n-1:
        c+=1
    else:
        r+=1
        c=0
for num in C:
    print(*num)
