    from sys import stdin
    input=stdin.readline
    n=int(input())
    arr=list(map(int,input().split()))

    def merge(arr):
        if len(arr)<2:
            return arr
        mid=len(arr)//2
        arr1=merge(arr[:mid])
        arr2=merge(arr[mid:])

        new_arr=[0]*len(arr)

        idx1=0
        idx2=0
        idxn=0

        while idx1<len(arr1) and idx2<len(arr2):
            if arr1[idx1]<arr2[idx2]:
                new_arr[idxn]=arr1[idx1]
                idx1+=1
                idxn+=1
            else:
                new_arr[idxn]=arr2[idx2]
                idx2+=1
                idxn+=1

        while idx1<len(arr1):
            new_arr[idxn]=arr1[idx1]
            idx1+=1
            idxn+=1
            
        while idx2<len(arr2):
            new_arr[idxn]=arr2[idx2]
            idx2+=1
            idxn+=1
     
        return new_arr

    l=0
    r=n-1
    mn=(2*10**10+1,0,0)
    arr=merge(arr)
    while l<r:
        now=(abs(arr[l]+arr[r]),arr[l],arr[r])
        mn=min(now,mn)
        if abs(arr[l+1]+arr[r])<now[0]:
            l+=1
        elif abs(arr[l]+arr[r-1])<now[0]:
            r-=1
        else:
            l+=1
            r-=1
            
    print(mn[1],mn[2])
