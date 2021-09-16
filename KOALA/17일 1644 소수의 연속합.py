n=int(input())

#에라..의 채
prime=[1 for i in range(n+1)] # n까지 수의 범위
for i in range(2,int(n**0.5)+1): # 소수 판정을 위해 사용할 수의 범위 sqrt(n)
    if prime[i]==1:
        for j in range(i*2,n+1,i): # i 의 배수들 지워나가기
            prime[j]=0
prime=[i for i in range(2,n+1) if prime[i]==1]

cnt=0 # n과 같은 횟수 저장
l,r=0,0 # 투 포인터?
total=0 # 합 저장

while ==len(prime): # 포인터중 작은 값이 최댓값이 될 경우?
    if total==n: # 합이 n인 경우
        cnt+=1
    if total<n: # 합이 n보다 작은 경우
        if r<len(prime): # 만들어놓은 소수의 범위 안에 r이 존재하는 경우
            total+=prime[r]
            r+=1
        else: # r이 만들어놓은 소수 중 가장 큰 값을 가졌었는데 그보다 큰 수를 요구하는 경우
            break
    else:
        total-=prime[l]
        l+=1

print(cnt)
