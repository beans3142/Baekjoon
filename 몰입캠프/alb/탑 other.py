n=int(input())
stack=[]
arr=list(map(int,input().split()))
ans=[0]*n
idx=0
for i in range(n):
    if stack and stack[-1][0]>arr[i]:
        ans[i]=stack[-1][1]+1
        stack.append([arr[i],i])
    else:
        while stack and stack[-1][0]<arr[i]:
            stack.pop()
        if stack:
            ans[i]=stack[-1][1]+1
        stack.append([arr[i],i])

print(*ans)
