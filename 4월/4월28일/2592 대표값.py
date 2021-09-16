#https://www.acmicpc.net/problem/2592

numlist=[] # 빈 리스트 <- 시퀀스형 데이터 = 여러개값을 저장가능!
common={} # 빈 세트 시퀀스 => 4 가지 문자열='ㅁㅇ잦망'
            #세트={}중복허용안되는 리스트, 키와 밸류 1:[2,3]
            #리스트 [1,2,3,51,2,5] 튜플(1,2,5)=> 수정불가능

for i in range(0,10): # 10번 반복
    num=int(input()) # num변수<=정수(입력을 받는다)
    numlist.append(num) # 추가

print(sum(numlist)//10) # sum(합)//개수 => 평균

for i in set(numlist): # 리스트 -> 세트 리스트 안에 있는 숫자를 i에 대입한다는 1, 2, 5 ,7 
    common[i]=numlist.count(i) # [1,2,5,7]

c=max(common.values()) # 1:5 2:3 4:0

for i in set(numlist):
    if common[i]==c: # 이숫자에 해당이 이거면
        print(i) # 출력해라 이거를
        break # 부서라 = 프로그램을 종료해라
