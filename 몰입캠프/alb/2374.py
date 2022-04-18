from sys import stdin
input=stdin.readline

n=int(input())
arr=[int(input()) for i in range(n)]
ans=0
stack=[arr[0]]
idx=1
while idx<n:
    if arr[idx]<stack[-1]:
        stack.append(arr[idx])
    elif arr[idx]>stack[-1]:
        ans+=arr[idx]-stack[-1]
        while stack and stack[-1]<=arr[idx]:
            stack.pop()
        stack.append(arr[idx])
    idx+=1
if stack:
    ans+=stack[0]-stack[-1]

print(ans)
