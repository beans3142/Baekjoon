import sys
input=sys.stdin.readline

n=int(input())

arr=[int(input()) for i in range(n)]
do=['+']
nl=list(range(2,len(arr)+1))
stack=[0,1]

idx=0


while len(do)<n*2:
    try:
        if arr[idx] != stack[-1]:
            stack.append(nl.pop(0))
            do.append('+')
        elif arr[idx] == stack[-1]:
            do.append('-')
            idx+=1
            stack.pop(-1)
    except IndexError:
        break

if len(do)==n*2:
    for i in do:
        print(i)
else:
    print('NO')
