from sys import stdin
input=stdin.readline

# 위치와 숫자가 일치하면 스트라이크, 숫자만 일치하면 볼이다.
# 총 가능한 경우의 수는 111~999사이의 0이 들어가지 않는 수 (9**3)개
# 충분히 완전탐색으로 가능한 문제이다.

# 질문에 대한 답변을 만족하는 숫자를 찾으면 된다.
# 앞서 말한 가능한 경우의 수에 대해 모두 답변에 대조해보면 된다.

n=int(input())

def check(x,y):
    strike=0
    ball=0
    for i in x:
        if i in y:
            ball+=1

    for i in range(3):
        if x[i]==y[i]:
            strike+=1
            ball-=1

    return strike,ball

cnt=0 # 가능한 정답의 개수
cmp=[]

for i in range(n):
    ans,s,b=input().rstrip().split()
    ans=[*map(int,list(ans))]
    s=int(s)
    b=int(b)
    cmp.append([ans,s,b])

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==k or j==k or j==i:
                continue
            able=True
            for case in cmp:
                if check([i,j,k],case[0])!=(case[1],case[2]):
                    able=False
                    break
            if able:
                cnt+=1

print(cnt)

'''
중복 및 0 처리
in
2
123 0 0
456 0 0

out
6

Wa - 중복 처리 안햇을 경우
27
Wa - 0을 포함시켰을 경우 (중복처리 O)
24
Wa - 위 두가지 모두 하지 않았을 경우
64
'''
