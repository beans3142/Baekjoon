# 매우 간단한 문제
# 그냥 뒤에서부터 스택에 집어넣어주면 된다.

# 스택의 top에 있는 값보다 큰 값이 들어오면 그 위치를 저장하고 pop해준다.

n=int(input())
towers=[(i,idx) for idx,i in enumerate(list(map(int,input().split())))]
stack=[]
ans=[0]*n
for i in range(n):
    while stack and stack[-1][0]<towers[~i][0]:
        val,loc=stack.pop()
        ans[loc]=towers[~i][1]+1
    stack.append(towers[~i])
print(*ans)
