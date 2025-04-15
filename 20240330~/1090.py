n=int(input())
x=set()
y=set()
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    x.add(a)
    y.add(b)
    arr.append((a,b))
ans=[]
mn=1e15
for k in range(n):
    mn=1e15
    for i in x:
        for j in y:
            case=[]
            for a,b in arr:
                case.append(abs(a-i)+abs(b-j))
            case.sort()
            s=sum(case[:k+1])
            if s<mn:
                mn=s
    ans.append(mn)
print(*ans)
