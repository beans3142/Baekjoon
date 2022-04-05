s=input()
le=len(s)
stack=[]
order=[chr(i) for i in range(97,97+len(s))]

noworder=0
ans=[]

for i in order:
    stack.append(i)
    ans.append('push')
    while stack and noworder<le and stack[-1]==s[noworder]:
        noworder+=1
        stack.pop()
        ans.append('pop')

if stack:
    print('impossible')
else:
    for i in ans:
        print(i)
