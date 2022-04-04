from time import *

#https://www.acmicpc.net/problem/2775
# 부녀회장이 될테야
# 조건 a층의 b호에 살기 위해선 a-1층의 1~b호의 사람들만큼 데려와야 함
# 아파트는 0층부터 시작, 각 층은 1호부터 존재, 0층의 i호에는 i명이 산다
'''
import sys ; input = sys.stdin.readline

t=int(input())

# for 문 중첩 O(n^2)
# 직접 아파트를 만드는 방식
# 뭔가 x,y를 뒤바꿔서 코드를 짠 듯 , 귀찮아서 안고칠꺼

for i in range(t):
    k=int(input())
    n=int(input())
    apart=[[0]]*(k+1)
    for i in range(k+1):
        floor=[]
        for j in range(n+1):
            if i==0:
                floor.append(j)
            else:
                floor.append(sum(apart[i-1][:j+1]))
        apart[i]=floor
    print(apart[k][n])
'''            
'''
for i in range(t):
    k=int(input())
    n=int(input())
    floor=list(range(0,n+1))
    for _ in range(1,k):
        for j in range(n):
            floor[n-j]=sum(floor[:n-j+1])
    print(sum(floor))
'''
#https://www.acmicpc.net/problem/1929

# O(n^3/2) ?
# 공통으로 맨앞에 두는거=> m,n=map(int,input().split())
'''
m,n=map(int,input().split())

def isp(x):
    if x==1:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        return True

for i in range(m,n+1):
    if isp(i):
        print(i)
'''


'''
start=time()
for i in range(m,n+1):
    if i > 1:  
        is_prime=True
        for j in range(2,int(pow(i,0.5))+1):
            if i%j==0:
                is_prime=False
                continue
        if is_prime:
            print(i)
print(time()-start)
'''
# O(n^3/2)의 절반?
# 시간 초과 발생
'''
start=time()
for i in range(m,n+1):
    if (i > 1 and i%2!=0) or i==2:  
        is_prime=True
        for j in range(2,int(pow(i,0.5))+1):
            if i%j==0:
                is_prime=False
                continue
        if is_prime:
            print(i)
print(time()-start)
'''
# 밀러 라빈 소수 판별법 => 완벽이해 X 아직
# 틀림 떴음...

#m,n=map(int,input().split())
'''
from random import randint

def miller_rabin_is_prime(number, k=10):
    if number < 2: # 입력받은 수가 2미만이면 예외처리
        return False
    elif number <= 3:
        return True # 입력받은 수가 2,3이면 예외처리 True
    else:
        odd_num = number - 1 # number 이 홀수인 경우? 짝수로 바꾼건가?
        power_of_two = 0 # 2의 제곱?
        while odd_num % 2 == 0:  # number이 짝수인 동안 (2로 나누어지는 동안)
            power_of_two += 1 # 2로 나눈 횟수를 +1
            odd_num //= 2 # odd_num을 2로 나눠줌
        for _ in range(k): # k 범위 안에서 반복(k=10으로 입력되어있다.)
            random = randint(2, number - 2) # 입력받은? 함수에 들어온
                                            # (number - 2) 와 2 사이의 랜덤 숫자
            checker = pow(random,odd_num, number) # 변수 checker은 위에서 정해진
                                                  # 변수 랜덤의 odd_num 제곱을
                                                  # number로 나눈 나머지
            if (checker == 1) or (checker == number - 1): # 체커는 1 또는 -1
                continue # 스킵
            try: #try
                for loop in range(power_of_two - 1):
                    # number보다 작은 가장 큰 2의 n제곱의 n 만큼
                                                    
                    checker = pow(checker,2,number)
                    # 체커는 체커의 제곱을 number로 나눈 나머
                    if checker == number - 1: # 변수 체커가 number-1과 같다면
                        # 어떤 수 (2,number-2)의 number-1제곱을 넘버로 나눈 값의
                        # 제곱과 같다면 
                        raise TypeError # 타입에러 일으킴
            except TypeError: 
                continue # 스킵
            return False # 거짓 반환 
        return True #print(number) # 참 반환
start=time()
for i in range(m,n+1):
    miller_rabin_is_prime(i)
print(time()-start)
'''
# 리스트를 제거해 가면서 사용 # 시간초과 발생
'''
start=time()
nl=[i for i in range(2,n+1)]

while nl:
    i=nl.pop(0)
    nl=[j for j in nl if j%i != 0]
    if i>=m:
        print(i)
print(time()-start)
'''
#https://www.acmicpc.net/problem/4948
#n과 2n사이의 소수

#시간 초과
'''
import math
import sys

input=sys.stdin.readline

while True:
    n=int(input())
    if n==0:
        break
    num=0
    if n==1:
        num=1
    for i in range(n+1,2*n+1):
        if i % 2 == 1:
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    break
            else:
                num+=1
    print(num)
'''
#  미리 소수 구해놓고 쓰기 # 에라스토네스의 채
'''
import sys
from math import sqrt

input=sys.stdin.readline

int_list=[True for _ in range(123456*2)]

for i in range(2,int(sqrt(123456*2))):
    if int_list[i]:
        for j in range(i+i,123456*2,i):
            int_list[j]=False

prime_list=[i for i,j in enumerate(int_list)if j and i>=2] # i < 2 = 0, 1

while True:
    gaesoo=0
    n=int(input())
    if not n:
        break
    for i in prime_list:
        if i<=n:
            continue   
        elif n*2>=i>n:
            gaesoo+=1
    print(gaesoo)
'''
# 일일히 찾는 방법 
'''
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    gold=[]
    for i in range(2,n//2+1):
        is_p=True
        for j in range(int(n**0.5),1,-1):
            if i%j==0 or (n-i)%j==0:
                if i != j and n-i != j:
                    is_p=False
                    break
        if is_p:
            print(i,n-i)
            break
'''
arr=[True for i in range(10001)]

arr[0]=False
arr[1]=False

for i in range(2,10001):
    if arr[i]==True:
        for j in range(i+i,10001,i):
            arr[j]=False


# 2775 1929 4948 9020(미해결)
