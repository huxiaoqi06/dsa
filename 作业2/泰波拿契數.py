n=int(input())
a=0
b=1
c=1
if n==1 or n==2:
    print(1)
else:
    for i in range(2,n):
        a,b,c=b,c,a+b+c
    print(c)