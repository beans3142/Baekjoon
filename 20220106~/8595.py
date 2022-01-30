n=int(input())
arr=[]
s=input()
ans=0
hid=''
for i in s:
    if i.isdigit():
        hid+=i
    else:
        if hid.isdigit():
            if len(hid)>6:
                hid=''
            else:
                ans+=int(hid)
                hid=''

if hid.isdigit():
    if len(hid)>6:
        hid=''
    else:
        ans+=int(hid)
        hid=''

print(ans)
