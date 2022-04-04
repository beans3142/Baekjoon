import sys
input=sys.stdin.readline

n=int(input()) # 시도 횟수
stack=[]

for i in range(n):
    scan=input().rstrip().split()
    if len(scan)>1:
        stack.append(int(scan[1]))
    else:
        scan=scan[0]
        if scan=='top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif scan=='size':
            print(len(stack))
        elif scan=='empty':
            if len(stack)==0:
                print(1)
            else:
                print(0)
        else:
            if len(stack)==0:
                print(-1)
            else:
                print(stack.pop(-1))
