import sys

input=sys.stdin.readline

n,m=map(int,input().split())

chess=[]
p1_cnt=0
p2_cnt=0

for i in range(n):
    chess+=list(input())

pattern1=[]
pattern2=[]


pattern1+=['W','B']*(m//2)
if m%2:
    pattern1+=['W','B']*(m//2)
else:
    pattern1+=reversed(['W','B']*(m//2))

pattern2+=['B','W']*(m//2)
if m%2:
    pattern2+=['B','W']*(m//2)
else:
    pattern2+=reversed(['B','W']*(m//2))


for i in range(len(chess)):
    if chess[i] != pattern1[i%len(pattern1)]:
        p1_cnt+=1
    if chess[i] != pattern2[i%len(pattern2)]:
        p2_cnt+=1

print(min(p1_cnt,p2_cnt))
