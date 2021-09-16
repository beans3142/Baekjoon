
#scores=[]
total=0

# 1차시도 (쓸데없이 리스트 사용)
'''
for i in range(5):
    scores.append(int(input()))

for score in scores:
    if score < 40:
        score=40
    total+=score

print(total//5)
'''

# 간소화 (리스트 제거, 변수 a추가)
for i in range(5):
    a=int(input())
    if a < 40:
        a=40
    total+=a

print(total//5)

# 주워온 코드 (변수 a도 제거, 거의 최적이라 생각) 부럽다;
'''
s = 0
for i in range(5) :
	s += max(40, int(input()))
print(s/5)
'''
