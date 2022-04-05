n,q=map(int,input().split())
arr=list(map(int,input().split()))
query=list(map(int,input().split()))

def binary_search(x):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if x<arr[mid]:
            r=mid-1
        elif arr[mid]==x:
            return True
        else:
            l=mid+1
    return False
            
    

for i in query:
    print("YES" if binary_search(i) else "NO")

'''
맨 오른쪽까지 완벽하게 정렬
in
10 5
1 2 4 8 10 11 12 14 15 19
4 5 8 17 19

out
YES
NO
YES
NO
YES

in
5 3
1 2 4 5 7
1 2 3

out
YES
YES
NO
'''
