from sys import stdin
input=stdin.readline

s=input().rstrip()
stack=[]

for i in range(len(s)):
    if stack and stack[-1]=='(' and s[i]==')':
        stack.pop()
    else:
        stack.append(s[i])

print(len(stack))
