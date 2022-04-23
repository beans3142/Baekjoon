from sys import stdin
input=stdin.readline

n=int(input())
cnt=0

for i in range(n):
    stack=[]
    s=input().rstrip()
    for i in s:
        if stack:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if not stack:
        cnt+=1

print(cnt)
    
