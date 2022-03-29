from sys import stdin
input=stdin.readline

# n줄에 걸쳐 RGB값 입력받음.
# 추가적으로 곰두리값 한줄을 더 입력받음
# n개의 물감을 섞어(최소 2 최대 7) 만들 수 있는 물감 중
# 곰두리값과의 차이가 가장 작은 값 출력
# 더하고 나눈 값을 넘겨주면 안된다. (= 매번 소수점을 버리면 안되고 마지막에만)

n=int(input())
inks=[] # 입력받은 rgb값을 저장해줄 배열

for i in range(n):
    r,g,b=map(int,input().split()) # rgb값 입력받음
    inks.append([r,g,b])

gomduri=list(map(int,input().split()))

ans=1000 # 가능한 값이 255, 255, 255이고 곰두리 값이 0, 0, 0이여도 최대 차이는 255*3밖에 안됨.

def bt(mixtime,nowrgb,idx): 
    global ans
    # 조합 횟수와 현재 rgb값과 들어간
    # rgb값중 가장 뒤의 인덱스 + 1을 인자로 전달해줌
    if 1<mixtime:
        dif=0
        for i in range(3):
            dif+=abs(nowrgb[i]//mixtime-gomduri[i]) # 현재 각 rgb값의 합 // 조합횟수
        ans=min(ans,dif)
        if mixtime==7: # 합쳐진 값의 수가 7개이면
            return
    for i in range(idx,n):
        newrgb=[]
        for j in range(3): # 3번
            newrgb.append(nowrgb[j]+inks[i][j])
        bt(mixtime+1,newrgb,i+1)
        
        
for idx,ink in enumerate(inks):
    bt(1,ink,idx+1)

print(ans)
