from sys import stdin
input=stdin.readline

def bf():
    for i in range(1,n+1):
        for j in range(1,n+1):
            for w,v in val[j]:
                if dist[v]>w+dist[j]:
                    dist[v]=w+dist[j]
                    if i==n:
                        print('YES')
                        return
    print('NO')
    return 
                    

for i in range(int(input())):
    n,m,w=map(int,input().split())
    dist=[10**9 for i in range(n+1)]
    val=[[]for i in range(n+1)]
    for j in range(m):
        s,e,t=map(int,input().split())
        val[s].append((t,e))
        val[e].append((t,s))
    for j in range(w):
        s,e,t=map(int,input().split())
        val[s].append((-t,e))

    bf()
