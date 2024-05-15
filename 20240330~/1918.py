operators = {"/": 2, "*": 2, "+": 1, "-": 1, "(": 0}
stack = []
ss = input()
ans=[]
for s in ss:
    if s.isalpha():
        ans.append(s)
    elif s == "(":
        stack.append(s)
    elif s == ")":
        temp = stack.pop()
        while temp!="(":
            ans.append(temp)
            temp = stack.pop()
    else:
        while stack:
            if operators[stack[-1]] < operators[s]: break
            ans.append(stack.pop())
        stack.append(s)
 
while stack:
    ans.append(stack.pop())

print(''.join(ans))
