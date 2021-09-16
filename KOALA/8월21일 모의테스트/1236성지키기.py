n,m=map(int,input().split())
vn={i:0 for i in range(n)}
vm={i:0 for i in range(m)}

castle=[]
for i in range(n):
    line=input()
    for j in range(m):
        if line[j]=='X':
            vm[j]=1
            vn[i]=1

for i in range(n):
    n-=vn[i]

for i in range(m):
    m-=vm[i]

print(max(n,m))
