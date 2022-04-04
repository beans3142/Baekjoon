dice=map(int,input().split()) # a,b,c 는 각각 3개의 주사위 눈
dice=list(dice)
dice.sort()

# 피드백 : dice=list(map....) 도 가능하다함!

for num in dice:
    if dice.count(num)==3:
        print(10000+num*1000)
        break
    elif dice.count(num)==2:
        print(1000+num*100)
        break
    elif len(set(dice))==3: # 중복이 0개임을 확인하
        dice.sort()
        print(dice[-1]*100)
        break

#https://www.acmicpc.net/problem/2480
