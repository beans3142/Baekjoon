t=int(input()) # 정수형 입력 input() <- 입력 기본 형태는 string 정수
     
for i in range(t):
    r,s=input().split()
    for j in s:
        print(j*int(r),end='')
    print()
