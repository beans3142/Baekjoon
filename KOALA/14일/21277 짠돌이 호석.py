# 여러줄에 많이 입력받으므로 input 대신 readline이 좋을 것
# 1번째 퍼즐이 변의 길이 x1 y1이고 2번째 퍼즐의 변의 길이 x2 y2라고 할때

# 최대 넓이는 (x1+x2)*max(y1,y2) 와 (y1+y2)*max(x1,x2) 중 큰 값일 것?
# 혹시 모르니 마지막에 min으로 테스트 해봐도 좋을 듯

# 4개의 모서리에는 꼭짓점이 존재, 두 조각 모두 한변의 길이도 3보다 작은 경우
# 무조건 2*2 1*1 => 6칸 or 8칸 or 2칸
# 아닌 경우 꼭짓점이 아닌 부분에 하나하나 넣어 보면 될듯?
# (0,0),(0,m1),(n1,0),(n1,m1)가 아닌~

# 두 퍼즐 모두 회전시킬 필요는 없을 것 하나만 회전시키고 (*3)
# 남은 퍼즐 하나를 일일히 넣어보는 것

# 다 돌려보고 넣는데 걸리는 시간? 일단 한 블럭마다 넣고 테스트하는 경우
# 최악의 경우도 50*50 2500-4개 정도?

# 이렇게 푼다면 아마 이 문제는 브루트 포스 문제일 듯?

#1) 한 블럭을 회전시킨 모양 3개를 포함하여 미리 저장해 놓는다.
# ex ) s1=▶ s2=▲ s3=◀ s4=▼
# 안에 있는 0마다 작은 쪽의 퍼즐이 들어갈수 있는지 체크
# 만약 한 퍼즐이 한 퍼즐 안에 다 들어간다면 바로 반복문 탈출
# 아닌 경우 들어가지 못한 퍼즐의 x,y값을 큰 퍼즐의 변의 길이에 더해준뒤 곱한 값
# 매번 그렇게 나온 결과 값들을 min 연산시켜 최소값을 얻을 것

# 새로운 배열을 매번 생성하는데(<- 아마 비효율적..)
# 블럭1과 블럭2의 값을 참조했을 때 모두 1이면 탈출

#1-2) 4번 돌린 형태이므로 아마□□ 큰 블럭의 4배안에서? 가능할 것 같다..?
#                           ＃■□

# 구현 가능할까??..
"""
import sys 

input=sys.stdin.readline

# 퍼즐을 입력받아 퍼즐 하나를 돌린 4개 형태를 만드는 부분

y1,x1=map(int,input().split())
puzzle1=[input().rstrip() for i in range(y1)]

y2,x2=map(int,input().split())
puzzle2=[input().rstrip() for i in range(y2)]

four_shape=[]
four_shape.append([puzzle1,x1,y1])

for i in range(1,4):
    l1=len(four_shape[i-1][0][0])
    l2=len(four_shape[i-1][0])
    rotate=[]
    for j in range(l1):
        line=''
        for k in range(l2-1,-1,-1):
            line+=four_shape[i-1][0][k][j]
        rotate.append(line)
    four_shape.append([rotate,l2,l1])

for i in range(4):
    ackja=[]
    for j in range(four_shape[i][2]):
        ackja.append(four_shape[i][0][j]+'0'*x2)
    for j in range(y2):
        ackja.append('0'*(four_shape[i][1]+x2))
    four_shape[i][0]=ackja
'''
four_shape2=[]
four_shape2.append([puzzle2,x2,y2])

for i in range(1,4):
    l1=len(four_shape2[i-1][0][0])
    l2=len(four_shape2[i-1][0])
    rotate=[]
    for j in range(l1):
        line=''
        for k in range(l2-1,-1,-1):
            line+=four_shape2[i-1][0][k][j]
        rotate.append(line)
    four_shape2.append([rotate,l2,l1])
'''
mnsize=min((x1+x2)*max(y1,y2),(y1+y2)*max(x1,x2))

print(mnsize)

# 탐색 시작할 부분
rshape=puzzle2
rx=x2
ry=y2

#for rshape,rx,ry in four_shape2:
if True:
    for shape,x,y in four_shape:
        for i in range(y+y2):
            for j in range(x+x2):
                if not (shape[i][j]==rshape[-1][0] and shape[i][j]=='1'):
                    able=True
                    #y_over=ry-i-1 if ry-i-1>0 else 0
                    #x_over=rx+j-x if rx+j>x else 0
                    for Y in range(ry):
                        for X in range(rx):
                            if i+Y>=y+y2 and j+X<x+x2:
                                if shape[i-Y][j+X]=='1' and rshape[-1-Y][X]=='1':
                                    able=False
                                    break
                        if not able:
                            break
                    if able:
                        print(i,j,min(mnsize,max(max(y,y2),(y2+y-i-1))\
                                       *max(max(x,x2),(x2+x-j-1))))
                        if (y2+y-i-1)*(x2+x-j-1)>=max(x,x2)*max(y,y2):
                            mnsize=min(mnsize,max(max(y,y2),(y2+y-i-1))\
                                       *max(max(x,x2),(x2+x-j-1)))


print(mnsize)
"""
# 반례발견
'''
3 3
111
011
111
3 3
111
110
111

정답 = 15
내 코드 답 = 18
'''

import sys 

input=sys.stdin.readline

# 퍼즐을 입력받아 퍼즐 하나를 돌린 4개 형태를 만드는 부분

y1,x1=map(int,input().split())
puzzle1=[input().rstrip() for i in range(y1)]

y2,x2=map(int,input().split())
puzzle2=[input().rstrip() for i in range(y2)]

four_shape=[]
four_shape.append([puzzle1,x1,y1])

for i in range(1,4):
    l1=len(four_shape[i-1][0][0])
    l2=len(four_shape[i-1][0])
    rotate=[]
    for j in range(l1):
        line=''
        for k in range(l2-1,-1,-1):
            line+=four_shape[i-1][0][k][j]
        rotate.append(line)
    four_shape.append([rotate,l2,l1])

four_shape2=[]
four_shape2.append([puzzle2,x2,y2])

for i in range(1,4):
    l1=len(four_shape2[i-1][0][0])
    l2=len(four_shape2[i-1][0])
    rotate=[]
    for j in range(l1):
        line=''
        for k in range(l2-1,-1,-1):
            line+=four_shape2[i-1][0][k][j]
        rotate.append(line)
    four_shape2.append([rotate,l2,l1])

mnsize=min((x1+x2)*max(y1,y2),(y1+y2)*max(x1,x2))

# 탐색 시작할 부분

for rshape,rx,ry in four_shape2:
    for shape,x,y in four_shape:
        for i in range(y):
            for j in range(x):
                if True:
                    able=True
                    y_over=ry-i-1 if ry-i-1>0 else 0
                    x_over=rx+j-x if rx+j>x else 0
                    for Y in range(ry):
                        for X in range(rx):
                            if i-Y>=0 and j+X<x:
                                if shape[i-Y][j+X]=='1' and rshape[-1-Y][X]=='1':
                                    able=False
                                    break
                        if not able:
                            break
                    if able:
                        mnsize=min((x+x_over)*(y+y_over),mnsize)
                        
print(mnsize)
