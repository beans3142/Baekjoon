#https://www.acmicpc.net/problem/1655

#인터넷에서 가져온 코드
#heapq , 우선순위 큐
#https://inspirit941.tistory.com/200
'''
import sys
import heapq

left,right = [],[]

n=int(sys.stdin.readline())
for _ in range(n):
    num=int(sys.stdin.readline())
    if len(left)==len(right):
        #max_heap.
        heapq.heappush(left,(-num,num))
    else:
        #min_heap.
        heapq.heappush(right,(num,num))
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right,(left_value,left_value))
        heapq.heappush(left,(-right_value,right_value))
    
    print(left[0][1])
'''
#시간 초과가 발생함. 밑의 코드

import sys

n=int(sys.stdin.readline())
nl=[]

for i in range(1,n+1):
    nl.append(int(sys.stdin.readline()))
    mid=i//2
    if i%2==0:
        mid-=1
    print(sorted(nl)[mid])

    
'''

#비슷한 문제 : 키로거
#https://www.acmicpc.net/problem/5397
'''
