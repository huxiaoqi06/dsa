n=int(input())
prime=[1]*(n+1)
prime[0]=prime[1]=0
for i in range(2,int(n**0.5)+1):
    if prime[i]:
        for j in range(i**2,n+1,i):
            prime[j]=0
for i in range(n+1):
    if prime[i] and prime[n-i]:
        print(i,end=' ')
        print(n-i)
        break