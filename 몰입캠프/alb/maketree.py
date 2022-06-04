n=int(input())

tree=[[] for i in range(n)] # 1부터 시작이면 n+1, 0부터 시작이면 n

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a) # a, b가 부모 - 자식 관계라면 해당 부분 주석 처리

