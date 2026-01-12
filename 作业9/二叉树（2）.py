def f(x):
    i=0
    while True:
        if 2**i-1<x<=2**(i+1)-1:
            return i
        i+=1
while True:
    m,n=map(int,input().strip().split())
    if m==0 and n==0:
        break
    i=f(m)
    j=f(n)
    num=2**(j-i)-1
    front=(m-1-2**i+1)*2**(j-i)
    res=n-2**j+1
    if res<=front:
        pass
    elif front<res<front+2**(j-i):
        num+=res-front
    else:
        num+=2**(j-i)
    print(num)