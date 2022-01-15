from sys import stdin
from collections import defaultdict
input=stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]

n=int(input())
# 선호하는 사람들을 나타내줄 딕셔너리
# like[사람][이 사람을 좋아하는 사람]으로 이용 (0=안좋,1=좋)
# 사람 수는 고정적이고 번호도 고정적임
like={i+1:defaultdict(int) for i in range(n**2)}
# 정답 배열
arr=[[0 for i in range(n)]for i in range(n)]

# 입력받고 like를 채워나가기
# defaultdict의 특징 활용

order=[] # 사람을 채워나갈 순서를 담을 배열
for i in range(n**2):
    research=list(map(int,input().split()))
    for j in range(1,5):
        like[research[j]][research[0]]+=1
    order.append(research[0])

# 우선순위 파악을 잘 해야함
# 1순위 = 인접한 좋아하는 사람의 수
# 2순위 = 비어있는 칸의 수
# 3순위 = y좌표
# 4순위 = x좌표

# 3,4순위가 작을수록 앞에 오게 만들 생각이므로 오름차순 정렬을 할 것.
# 그러므로 1순위와 2순위의 값을 음수로 활용할 것이다.
# 후보군을 배열에 넣고 정렬해 줄 예정이다.
# 후보군은 다음과 같은 값을 갖는다.
# [-1*좋아하는 사람의 수,-1*비어있는 칸의 수,y좌표,x좌표]

for no in order: # order의 사람들을 채울때 까지만 반복하면 되므로
    vals=[]
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                val=[0,0,i,j]
                for k in range(4):
                    ni=i+dy[k]
                    nj=j+dx[k]
                    if -1<ni<n and -1<nj<n:
                        if arr[ni][nj]:
                            val[0]-=like[arr[ni][nj]][no]
                        else:
                            val[1]-=1
                vals.append(val)
    vals.sort()
    arr[vals[0][2]][vals[0][3]]=no

# 점수 계산

totalscore=0

for x in range(n):
    for y in range(n):
        cnt=0 # 인접한 좋아하는 사람의 명수
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n:
                here=arr[y][x]
                near=arr[ny][nx]
                cnt+=like[near][here]
        totalscore+=10**(cnt-1) if cnt!= 0 else 0

print(totalscore)
