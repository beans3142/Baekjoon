# n을 입력받고 n번 뒤집는다
# i가 0~n까지
# 단순 브루트포싱으로 해결가능
# 행렬 뒤집기 1번 문제랑 똑같고 입력만 제대로 받아주면 됨.

n=int(input())
arr=[list(map(int,input().split())) for i in range(10)]
for i in range(n):
    for j in range(10): # 어떻게든 뒤집기만 하면 됨.
        arr[j][i]^=1
        arr[i][j]^=1
    arr[i][i]^=1
        
for i in arr:
    print(*i)

'''

'''
