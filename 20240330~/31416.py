from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    ta,tb,va,vb=map(int,input().split()) # "ta=1_tb=2_va=3_vb=4"
    ma=0 # make a
    mb=0 # make b
    # 
    # ta=2 시간10 5번수행가능 시간/걸리는시간
    for i in range(1,100000): # i가 시간
        ma=i//ta # 시간을 a를 만드는데 걸리는 시간으로 나누면 a가 몇개 만드는지
        mb=i//tb # mb도 마찬가지
        ha=max(0,(i-tb*vb)//ta) # 도울수 있는건
        # i-tb*vb tb*vb<i 만들어야하는개수*만드는데걸리는시간 < 현재 시간
        # 
        if ma+ha>=va and mb>=vb:
            break
    print(i)
