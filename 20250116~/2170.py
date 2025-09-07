from sys import stdin;input=stdin.readline

# 입력 받는 부분
n=int(input())
lines=sorted([list(map(int,input().split())) for i in range(n)])

# 앞으로 저 입력받은 줄들을 묶어줄거임.
# 입력 기준 
# 1 3
# 2 5
# 3 5
# 6 7
# 일때 
# 1 5
# 6 7
# 이렇게 2개로 바꾸겠다~

# 일단 시작은 처음 값으로 시작
# nowline은 묶어주는? 선분, 아직 완전한 선분이 아니라
# 스위핑을 진행하며 선분 여러개를 묶어놓는 변수?
nowline=lines[0]

# 스위핑 한 후 배열
sweeped_lines=[]

for i in range(1,n): # 처음껀 했으니까~
    if nowline[1]<lines[i][0]: # 현재 묶고있던 선분의 끝보다 i번째 선분의 시작 좌표가 크다면 (같으면 묶을 수 있으니)
        sweeped_lines.append(nowline) # 묶어놓은 그룹을 배열에 추가한다.
        nowline=lines[i] # line[i]부터 다시 묶기 시작
    else: # 이 시점에서, lines[i][0]은 nowline[1]보다 작다는것이 증명됨, if문이 그러니까. 
        nowline[1]=max(nowline[1],lines[i][1]) # 새로 묶는 선분의 끝과 기존 선분의 끝을 비교해서 업데이트

sweeped_lines.append(nowline) # 마지막에 무조건 해줘야 함. 이건 생각해보면 답이 나온다. (ex 하나로 묶는다면?, nowline이 비어있는 경우는 없다)

# 이렇게 for문으로 한번 쓸었다(sweep)해서 스위핑이다.

ans=0
for line in sweeped_lines:
    ans+=line[1]-line[0] # 길이 더해준다
print(ans)
