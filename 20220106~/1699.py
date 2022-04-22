# DP 문제
# 무조건 큰 수를 넣는다고 효율이 좋아지는 것이 아님
# ex ) 23의 경우 9 + 9 + 4 + 1 로 표현이 가능
# 23보다 작은 가장 큰 제곱수인 16을 넣는 경우 16+4+1+1+1로 위의 예시보다 큼
'''
n=int(input())
arr=[i for i in range(n+1)]
scope=int(n**0.5)+1
for i in range(scope):
    arr[i**2]=1

for i in range(1,n+1):
    for j in range(1,scope):
        if i<j**2:
            break
        arr[i]=min(arr[i],arr[i-j**2]+1)

print(arr[i])
'''

# 라그랑주 네 제곱수 정리에 따른 풀이.]
'''
n=int(input())
arr1={i**2 for i in range(1,int(n**0.5)+1)}
if 0 in arr1:
    print(1)
arr2={n-i for i in arr1}
if 0 in arr2:
    print(2)
arr3={i-j for i in arr1 for j in arr2}
if arr3&arr1:
    print(3)
else:
    print(4)
'''
from collections import defaultdict
n=int(input())
dd=defaultdict(int)
scope=int(n**0.5)+1
for i in range(scope):
    for j in range(scope):
        dd[i**2+j**2]=bool(i)+bool(j)

for i in range(scope):
    for j in range(scope):
        if dd[(i**2+j**2)]:
            print(bool(i)+bool(j)+dd[i**2+j**2])
            exit()
