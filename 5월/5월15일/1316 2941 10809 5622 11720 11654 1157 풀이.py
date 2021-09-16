
#https://www.acmicpc.net/problem/1157
# 단어 공
'''
word=list(input().lower())

#word=word.lower()

#word=list(word)

n=0
w=''

for i in set(word):
    if n < word.count(i):
        n=word.count(i)
        w=i
    elif n == word.count(i):
        w='?'

print(w.upper())
'''
#https://www.acmicpc.net/problem/11654
# 아스키 코드 # 아스키 코드 응용 방안 다양해보임 ★
'''   
w=input()

print(ord(w))

print(ord(input())) #숏코딩
'''
#https://www.acmicpc.net/problem/11720
# 숫자의 합
'''
n=int(input())
arr=input()
total=0
for i in range(n):
    total+=int(arr[i-1])

print(total)
'''
#https://www.acmicpc.net/problem/5622
# 다이얼 # 아스키 코드 활용해서도 풀이 가능!
'''
w=input()

#dial={'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5\
      ,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9\
      ,'Y':9,'Z':9} 아스키 코드 활용 X 일일히 다침 
      
dial={}
asci=65
n=0
while True:
    dial[chr(asci)]=2+n//3
    if asci != 82 and asci != 87:
        n+=1
    asci+=1
    if asci == 91:
        break

total=0

for i in w:
    total+=dial[i]+1

print(total)
'''

#https://www.acmicpc.net/problem/10809
# 알파벳 찾기 # 3단계에 걸쳐 코드를 줄임
# 1은 밑의 코드 2는 print문 내에서 조건을 2개 걸어서 사용 > 과 <
# 3 은 밑의 코드 print문 내에서 하나의 조건과 or을 이용
'''
s=input()

a_to_z=[chr(i) for i in range(97,123)]

for i in a_to_z:
    if s.count(i) == 0:
        print(-1,end=' ')
    else:
        print(s.index(i),end=' ')

s=input()
for i in [chr(i)for i in range(97,123)]:
    print(str(s.find(i))*(s.count(i)>0)or-1,end=' ')
'''
#https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳
'''
croatia=('dz=','d-','lj','c=','c-','nj','s=','z=')
w=input()
total=len(w)

for i in croatia:
    n=w.count(i)*(len(i)-1)
    if i == 'z=':
        n=(w.count(i)-w.count('dz='))*(len(i)-1)
    total-=n
    
print(total)
'''
#https://www.acmicpc.net/problem/1316
# 그룹 단어 체커
'''
t=int(input())
num=0
for i in range(t):
    word=input()
    is_group=True
    arr=[word[0]]
    for j in range(1,len(word)):
        if word[j] not in arr:
            arr.append(word[j])
        else:
            if word[j]!=word[j-1]:
                is_group=False
                continue
    if is_group:
        num+=1

print(num)
'''

# 1316 2941 10809 5622 11720 11654 1157 풀이
