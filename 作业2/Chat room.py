s=input()
n=0
a=["h","e","l","l","o"]
for i in range(len(s)):
    if s[i]==a[n]:
        n+=1
        if n==5:
            break
if n==5:
    print("YES")
else:
    print("NO")