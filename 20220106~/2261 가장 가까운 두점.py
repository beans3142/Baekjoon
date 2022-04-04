from sys import stdin
input=stdin.readline

ans=10**10
py=[]
px=[]
n=int(input())

for i in range(n):
    x,y=map(int,input().split())
    py.append([y,x])
    px.append([x,y])
    
py.sort()
px.sort()

for i in range(n-1):
    ans=min(ans,(py[i][0]-py[i+1][0])**2+(py[i][1]-py[i+1][1])**2)
    ans=min(ans,(px[i][0]-px[i+1][0])**2+(px[i][1]-px[i+1][1])**2)

print(ans)

# 분할 정복을 이용해서 푸는 문제. 조금 더 공부해서 다시 풀어보
