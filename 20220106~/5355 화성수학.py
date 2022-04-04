n=int(input()) # 테스트 케이스 갯수 입력

mars=0 # 값을 저장할 곳

for i in range(n): # 테스트 케이스의 갯수만큼 반복
    a=input().split() # 첫 자리는 소수or정수 입력
    mars=float(a[0]) # 첫 수 저장
    for j in a: # a안에 있는 문자열들을 j에 저장
        if j == '@': # 그 문자열이 ~ 라면 각각에 맞는 수행
            mars*=3
        elif j == '%':
            mars+=5
        elif j == '#':
            mars-=7
    print('%.2f'%mars) # 소수점 둘째 자리까지만 출력
            
