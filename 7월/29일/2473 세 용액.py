import sys
from bisect import bisect_left
input=sys.stdin.readline

n=int(input())

arr=sorted(list(map(int,input().split())))
matrix=[[0 for j in range(n)]for i in range(n)]
l,r=0,n-1
mn=10**9*4

while l<r:
    try:
        total=arr[l]+arr[r]
        m=bisect_left(arr,-total)
        m_list=[]
        if m!=n:
            m_list.append(m)
        m_list.append(m-1)

        for i in m_list:
            #print(arr[l],arr[r],arr[i])
            if i!=l and i!=r:
                print(total+arr[i],mn)
                if abs(total+arr[i])<mn:
                    mn=total+arr[i]
                    yongaek=arr[l],arr[i],arr[r]
                
        if l+1<r and abs(total-arr[l]+arr[l+1])<abs(total):
            l+=1
        elif r-1>l and abs(total-arr[r]+arr[r-1])<abs(total):
            r-=1
        else:
            l+=1
            r-=1
        print(yongaek)
    except:
        break

print(yongaek)
