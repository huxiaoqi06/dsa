import re
while True:
    try:
        s=input()
        ans=re.match("^([\w-]+\.*)*[\w-]+@[\w-]+(\.[\w-]+)+$",s)
        print(bool(ans))
    except EOFError:
        break