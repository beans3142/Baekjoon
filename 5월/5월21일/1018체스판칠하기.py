import sys
input=sys.stdin.readline

n,m=map(int,input().split())

chess=[list(input())[:-1]for i in range(n)]

each1=[[0 for i in range(m)]for i in range(n)]
each2=[[0 for i in range(m)]for i in range(n)]


pattern1=['W','B']*(m//2)
if m%2:
    pattern1+=['W']+['B','W']*(m//2)+['B']
else:
    pattern1+=reversed(['W','B']*(m//2))

pattern2=['B','W']*(m//2)
if m%2:
    pattern2+=['B']+['W','B']*(m//2)+['W']
else:
    pattern2+=reversed(['B','W']*(m//2))

for i in range(n):
    for j in range(m):
        if pattern1[i%2*m+j%m] != chess[i][j]:
            each1[i][j]=1
        if pattern2[i%2*m+j%m] != chess[i][j]:
            each2[i][j]=1

mn=64

for i in range(n-7):
    for j in range(m-7):
        case1=0
        case2=0
        for l in range(i,i+8):
            case1+=sum(each1[l][j:j+8])
            case2+=sum(each2[l][j:j+8])
        mn=min(mn,case1,case2)

print(mn)
