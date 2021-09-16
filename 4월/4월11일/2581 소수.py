import sys

n=int(sys.stdin.readline()) # 최솟값 입력
m=int(sys.stdin.readline()) # 최댓값 입력

l=set(i for i in range(n,m+1)) # n~m까지의 숫자입력

not_prime={1} # 빈 세트 not_prime 생성

for num in l: # l 안에 든 num 중
    for i in range(2,int(num**0.5)+1): # 2~루트num까지 i
        if num%i==0: # 그 i로 나눴을 때 0이면
            not_prime.add(num) # not_prime에 num을 저장

if len(l.difference(not_prime))==0: # 만약 not_prime과 l이 모두 겹친다면
    print(-1) # -1 출력
else: # 아니라면 
    print(sum(l.difference(not_prime))) # 소수의 합 출력
    print(min(l.difference(not_prime))) # 소수 중 최솟값 출력
