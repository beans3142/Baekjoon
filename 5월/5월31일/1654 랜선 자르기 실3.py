import sys
input=sys.stdin.readline

k,n=map(int,input().split())

arr=[int(input()) for i in range(k)]

mx=max(arr)
mn=1

while mn<=mx:

    #print(mn,mx)
    
    cm=0
    for i in arr:
        cm+=i//((mx+mn)//2)

    if cm<n:
        mx=(mx+mn)//2-1
    elif cm>=n:
        mn=(mx+mn)//2+1

print(mx)

'''

while True:

    #print(mn,mx)

    if mn==mx:
        break
    
    cm=0
    
    for i in arr:
        cm+=i//((mx+mn)//2)

    if cm>=n:
        mn=(mx+mn)//2
    elif cm<n:
        mx=(mn+mx)//2

print(mn)
'''

#mn=min(arr)
'''
while True: # 이러면 n^2꼴 k가 1만개 들어감=> 1억번 연산=> 시간초과 100%;;
    cm=0
    for i in arr:
        cm+=i//mn
    if cm>=n:
        break
    mn-=1
'''
    
    
