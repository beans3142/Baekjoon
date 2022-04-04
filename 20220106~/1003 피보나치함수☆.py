# 시간 초과 발생 ☆
fibo_list=[]

def fib(n):
    global a,b
    if n == 0:
        a+=1
        return 0
    elif n == 1:
        b+=1
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(int(input())))

#https://www.acmicpc.net/problem/1003

#1은 0을 제외 모든곳에 적어도 1개씩+쪼개지며 피보나치
    #3인 경우 1이 2개 0이 1개 이런식으로 0 이 한발자국 늦게 출발한다는 느낌
    #n-1개의 1의 개수와 n개의 0의 개수가 같음
