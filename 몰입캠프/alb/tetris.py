from sys import stdin
input=stdin.readline

# 테트리스 게임
# 블럭은 위에서 아래로 내려온다.
# 기울이기가 불가능하다.
# 놓을 수 있는 공간이 없거나 채워지는 라인이 없다면 0 0 을 출력해야 한다.
# 세로블럭의 크기는 1*4 사이즈이다.

# 맨 위에서 쭉 내려간다 했을 때 더이상 0이 아니거나
# 배열을 벗어나는 위치가 놓을 수 있는 곳이다.
# 즉 놓을 수 있는 곳은 최대 20칸에 불과하다.
# 그 20칸을 모두 구해준뒤 그곳으로부터 위로 4칸을 채워준다 가정하고 풀면 된다.
# 채워지는 라인의 경우 sum을 이용해서 해당 라인의 채워진 개수가
# c보다 1만큼 작은 경우이다.

# 사라지는 블럭의 수가 같을 수 없다.

c,r=map(int,input().split())
matrix=[list(map(int,input().split())) for i in range(r)]
placeAt=[-1]*c # 놓을 수 있는 위치를 표시해줄 배열

for i in range(c):
    for j in range(r):
        if matrix[j][i]==1: # 1을 마주한다면 1보다 한 칸위
            placeAt[i]=(i,j-1)
            break
    if placeAt[i]==-1: # 1이 존재하지 않았다면
        placeAt[i]=(i,r-1)

mxFilled=0
mxIdx=0
for i in range(c):
    filled=0
    x,y=placeAt[i]
    unable=False # 불가능한 경우 ( 맵을 벗어나는 경우 )
    for j in range(4): # 위로 4칸 체크
        if sum(matrix[y-j])==c-1: # 해당 라인이 한칸만 비어있는 경우
            filled+=1
        if y-j<0:
            unable=True
            break
    if not unable:
        if filled>mxFilled:
            mxIdx=i+1
            mxFilled=filled

print(mxIdx,mxFilled)

"""
TC

위에서 내려오게 코딩X or 갈수 없는 곳 체크
in
5 5
1 1 1 1 1
1 0 1 1 1
1 0 1 1 1
1 0 1 1 1
1 0 1 1 1

out
0 0

정상적인 게임오버 처리
in
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
1 1 1 1 1
out
0 0

위와 동일
in
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 0 0 1 0
1 0 0 1 0
out
0 0

제대로 작동
5 5
1 0 1 1 1
1 0 1 1 1
1 0 1 1 1
1 0 1 1 1
1 1 1 1 1

out
2 4
"""
        
