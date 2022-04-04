import sys
import heapq 

n=int(sys.stdin.readline())
for _ in range(n):
    left,right = [],[]
    l=int(sys.stdin.readline())
    print((l+1)//2)
    nums=[]
    cnt=0
    for i in range((l+9)//10):
        nums+=list(map(int,sys.stdin.readline().split()))
    for i,num in enumerate(nums):
        if len(left)==len(right):
            heapq.heappush(left,(-num,num))
        else:
            heapq.heappush(right,(num,num))
        if right and left[0][1] > right[0][1]:
            left_value = heapq.heappop(left)[1]
            right_value = heapq.heappop(right)[1]
            heapq.heappush(right,(left_value,left_value))
            heapq.heappush(left,(-right_value,right_value))
        if i%2==0:
            cnt+=1
            print(left[0][1],end=' ')
            if cnt%10==0:
                print()
    print()
