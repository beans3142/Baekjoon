#https://www.acmicpc.net/problem/10250

t=int(input()) # 테스트 케이스의 개수

for i in range(t):
    j=0
    h,w,n=map(int,input().split())
    hotel=[[100*i+j for j in range(w+1)] for i in range(h+1)]
    while True:
        j+=1
        if n<=h:
            break
        n-=h
    print(hotel[n][j])
