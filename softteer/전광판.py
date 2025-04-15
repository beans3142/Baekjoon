from sys import stdin
input=stdin.readline
'''
해당 위치를 비트로 생각
   0
   -
1 | | 2
   - 3
4 | | 5
   - 
   6
중요한건 입력받은 2개가 다르면 그 곳을 키거나 꺼야 함(1번 누른다는 이야기)
같으면 0, 다르면 1 -> 이게 뭐다 XOR 따라서 xor을 통해 구할 수 있다.
'''

def get2(n):
    cnt=0
    while n:
        cnt+=n%2
        n//=2
    return cnt

# 위 그림에서 켜진 비트
# 빈 블럭은 -로 처리해준다. 모두 꺼져있는 블럭
on={'-':[],'0':[0,1,2,4,5,6],'1':[2,5],\
    '2':[0,2,3,4,6],'3':[0,2,3,5,6],'4':[1,2,3,5],\
    '5':[0,1,3,5,6],'6':[0,1,3,4,5,6],'7':[0,1,2,5],\
    '8':[0,1,2,3,4,5,6],'9':[0,1,2,3,5,6]}
# 위 켜진 비트를 2진수로 바꿔줄거임(더빠르니까)
# ex 0은 0 1 2 3 4 6 이면 1110111로 바꾼다.
# 밑에가 그 과정
onbit={i:0 for i in on}
for i in on:
    for j in on[i]:
        onbit[i]|=(1<<j)

for _ in range(int(input())):
    n1,n2=input().rstrip().split()
    # 길이를 맞춰주기
    if len(n1)<5: n1='-'*(5-len(n1))+n1
    if len(n2)<5: n2='-'*(5-len(n2))+n2
    ans=0
    for i in range(5):
        xor=onbit[n1[i]]^onbit[n2[i]]
        ans+=get2(xor)
    print(ans)

'''
2
111 11
11 11111
'''
