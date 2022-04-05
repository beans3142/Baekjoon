ps=input()
stack=['']

for i in ps:
    if stack[-1]=='(' and i==')':
        stack.pop()
    else:
        stack.append(i)

if len(stack)==1:
    print('YES')
else:
    print('NO')

'''
TC
좌우 처리 안한 경우
in
)))(((

out
NO
'''
