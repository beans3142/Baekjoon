from sys import stdin
input=stdin.readline

try:
    n=int(input())
    arr=list(map(int,input().split()))
    preoddsum=[0,arr[0],arr[0]]
    preevensum=[0,0,arr[1]]
    for i in range(3,n+1):
        if i%2:
            preoddsum.append(preoddsum[-1]+arr[i-1])
            preevensum.append(preevensum[-1])
        else:
            preoddsum.append(preoddsum[-1])
            preevensum.append(preevensum[-1]+arr[i-1])

    cnt=0

    for i in range(1,n+1):
        s1=0
        s2=0
        s1+=preoddsum[i-1]+(preevensum[n]-preevensum[i])
        s2+=preevensum[i-1]+(preoddsum[n]-preoddsum[i])
        if s1==s2:
            cnt+=1
        
    print(cnt)
except:
    print(0)
