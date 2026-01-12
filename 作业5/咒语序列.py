s=input()
i=0
l=[-1]
c=0
m=0
while i<len(s):
    if s[i]=='(':
        c+=1
        l.append(i)
    else:
        if c>0:
            c-=1
            l.pop()
            m=max(m,i-l[-1])
        else:
            l=[i]
            c=0
    i+=1
print(m)