# 시간 내에 4백만 이하의 소수의 리스트를 구할 수 있을까?ㅁㄴㅇㄹ;;

from sys import stdin
input=stdin.readline

prime=[1 for i in range(4000001)]

for i in range(2,2000):
    if prime[i]==1:
        for j in range(i*2,4000001,i):
            prime[j]=0
prime=[i for i in range(2,4000001) if prime[i]==1]+[0,0]
n=int(input()) # 목표 숫자
cnt=0 # 몇번 가능한지 저장할 변수
l,r=0,0 # 포인터?
total=0 # l~r사이의 소수의 합 저장할 변수
'''
    while True:
        if n<l:
            break
        if total==n:
            cnt+=1
            total=0
            l=r-1
        while total<n:
            while prime[r]==0:
                r+=1
            total+=r
            r+=1
        while total>n:
            while prime[l]==0:
                l+=1
            total-=l
            l+=1
'''
while True:
    try:
        if prime[r-1]>n:
            break
        if total==n:
            cnt+=1
        if total<n or l==r:
            total+=prime[r]
            r+=1
        else:
            total-=prime[l]
            l+=1
    except:
        break
print(cnt)
