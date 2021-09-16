#https://www.acmicpc.net/problem/11729

import sys
input=sys.stdin.readline

t=int(input())

def hano(t,a,b,c):
    global i
    print(a,b,c)
    print('now t is',t)
    if t==1:
        print(a,c)
    else:
        hano(t-1,a,c,b)
        print(a,c)
        hano(t-1,b,a,c)

hano(t,1,2,3)

# 1, 2, 3 => 1, 3, 2 => 1, 3 와 1, 2 t=1 에서 시작되므로 1, 2, 3, 4, 5 이순서로.
# 1->3, 1->2 이게 실행되고 t=2 else에서 print(a,c) 실행 이후 t-1 b,a,c 실행됨
# 기존 a,b,c는 홀짝에 따라 배치되고, 1->2, 1->3 짝수기준 쨋든 그거에 따라
# t=3일때 들어가서 else 실행 (3,1,2,3)-> (2,1,3,2) -> (1,1,2,3) -> t==1 실행됨,
# a,c (1,3) 출력 => t==2일때 (2,1,3,2)에서 print(a,c) 실행됨=>(1,2) 출력
# hano(1,3,1,2)로 들어감 => (3,2) 출력, 이제 t==3에서 스킵되었던 부분 실행,

# 결론, 짝 홀에 따라 첫 번째 마지막 발판이 드러날때 b에 모두 모여있어야됨,
# 그것에 따른 반복
