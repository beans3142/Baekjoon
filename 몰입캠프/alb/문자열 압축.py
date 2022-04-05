s=input()
last=s[0]
stack=1
ans=''
for i in range(1,len(s)):
    if last==s[i]:
        stack+=1
    else:
        ans+=str(stack)+last if stack>1 else last
        last=s[i]
        stack=1
ans+=str(stack)+last if stack>1 else last
print(ans)
