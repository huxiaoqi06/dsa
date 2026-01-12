s=input()
l=[]
a=["A","E","I","O","U",'Y','a','e','i','o','u','y']
for i in range(len(s)):
    if s[i] not in a:
        b=s[i]
        if ord("A")<=ord(s[i])<=ord('Z'):
            b=chr(ord(s[i])-ord("A")+ord('a'))
        l.append(b)
for i in range(len(l)):
    print("."+l[i],end="")