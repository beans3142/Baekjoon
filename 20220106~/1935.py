from sys import stdin
input=stdin.readline

n=int(input())
stack=[]
sik=list(input().rstrip())
val={chr(65+i):int(input()) for i in range(n)}

for i in sik:
    if 'A'<=i<='Z':
        stack.append(val[i])
    else:
        n1=stack.pop()
        n2=stack.pop()
        if i=='+':
            stack.append(n1+n2)
        elif i=='-':
            stack.append(n2-n1)
        elif i=='*':
            stack.append(n1*n2)
        else:
            stack.append(n2/n1)

print("%0.2f"%stack[-1])
