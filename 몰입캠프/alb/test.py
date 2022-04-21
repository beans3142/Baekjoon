n=int(input())
towers=[(i,idx) for idx,i in enumerate(list(map(int,input().split())))]
stack=[]
ans=[0]*n
for i in range(n):
    while stack and stack[-1][0]<towers[~i][0]:
        val,loc=stack.pop()
        ans[loc]=towers[~i][1]+1
    stack.append(towers[~i])
    print(stack)
print(*ans)
