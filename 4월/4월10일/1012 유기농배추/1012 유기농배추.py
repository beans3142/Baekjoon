
for i in range(int(input())): # 테스트 케이스의 개수
    locate=[]
    m,n,k=map(int,input().split()) # m 가로 n 세로 k 배추의 개수 입력
    for j in range(k): # 배추의 갯수만큼 반복
        x,y=map(int,input().split()) # 위치 입력
        locate+=[[x,y]] # 위치 저장
    for l in locate:
        if [l[0],l[1]-1] in locate:
            print('sex')
    
    
