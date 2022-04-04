#https://www.acmicpc.net/problem/1011

t=int(input()) # 테스트 케이스의 개수

for i in range(t):
    x,y=map(int,input().split())
    l1=y-x
    k=0
    l2=0
    while l2<l1:
        k+=1
        l2+=(k+1)//2
    print(k)

# 1 2 2 1

# 2021/5/14 나 자신 ㅈ밥..
# 이걸 7트를 ㅋㅋㅋㅋㅋㅋ...
