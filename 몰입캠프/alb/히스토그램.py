from sys import stdin
input=stdin.readline

n=int(input())
stack=[0]
h=[0]+list(map(int,input().split()))+[0]
ans=0

for i in range(1,n+2):
    while stack and h[stack[-1]]>h[i]:
        num=stack[-1]
        stack.pop()
        ans=max(ans,h[num]*(i-stack[-1]-1))
    stack.append(i)

print(ans%((1<<31)-1))
