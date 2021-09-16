import sys
input=sys.stdin.readline

N=int(input())
matrix=[input().rstrip()for i in range(N)]

def divide(l,n):
    if True:
        part=[[],[],[],[]]
        for s in range(2):
            for x in range(2):
                for y in range(n):
                    part[2*s+x].append(l[y+s*n][n*x:n*(x+1)])
    return part
                

def check(l,n):
    is_perfect=True
    for i in range(1,n):
        for j in range(1,n):
            if l[0][0]!=l[0][j]:
                is_perfect=False
                break
        if l[0] != l[i] or not is_perfect:
            is_perfect=False
            break
    if is_perfect:
        if N==2:
            print('(',end='')
        print(l[0][0],end='')
        if N==2:
            print(')')
    else:
        if n>2:
            print('(',end='')
            div=divide(l,n//2)
            for i in div:
                #print(i)
                check(i,n//2)
            print(')',end='')
        else:
            print('(',*l[0],*l[1],sep='',end=')')
            
            
check(matrix,N)
