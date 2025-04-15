'''
from sys import stdin
input=stdin.readline
n=int(input())
arr=list(map(int,input().split()))
dic={i:0 for i in range(1000000)}
for i in range(n):
    if dic[arr[i]]:
        dic[arr[i]]-=1
        dic[arr[i]-1]+=1
    else:
        dic[arr[i]-1]+=1
ans=0
for i in dic:
    ans+=dic[i]
print(ans)
'''
from collections import defaultdict, deque

# 파일 읽기
with open("in.txt", "r") as file:
    n = int(file.readline().strip())  # 첫 줄 읽어서 정수형으로 저장
    arr = list(map(int, file.readline().strip().split()))  # 두 번째 줄 읽어서 정수 배열로 저장

def find(x, idx):
    while True:
        able = False
        if x - 1 in dd:
            for i in dd[x - 1]:
                if idx < i and arr[i] != -1:
                    arr[i] = -1
                    idx = i
                    able = True
                    x -= 1
                    break
        if not able:
            break

cnt = 0
dd = defaultdict(deque)

for i in range(n):
    dd[arr[i]].append(i)

order = sorted(dd, reverse=True)

for i in order:
    for j in dd[i]:
        if arr[j] != -1:
            arr[j] = -1
            find(i, j)
            cnt += 1

print(cnt)
