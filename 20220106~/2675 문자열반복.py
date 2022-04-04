t=int(input()) # 테스트 케이스 개수 입력

for i in range(t): # 테스트 케이스 개수 만큼 반복`
    s=input().split() # 숫자와 문자열 입력 / 숫자와 문자열 분리
    for w in s[1]: # 문자열 부분의 글자를 w에 저장
        print(w*int(s[0]),end='') # w를 받은 숫자만큼 반복해서 붙여서 출력
    print() # 한칸 띄
