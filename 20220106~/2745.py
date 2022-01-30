case={}
for i in range(10):
    case[str(i)]=i
for i in range(26):
    case[chr(65+i)]=10+i

s,b=input().split()
b=int(b)
ans=0
for i in range(len(s)):
    ans+=case[s[~i]]*(b**i)

print(ans)
