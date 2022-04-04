#https://www.acmicpc.net/problem/1037

n=int(input())
nl=list(map(int,input().split()))
real_n=max(nl)*min(nl)
    
print(real_n)


def quick2(nl): #배열 nl (정렬되지 않은 랜덤 리스트 또는 정렬중인 리스트)
    if len(nl)<=2: # nl의 길이가 3보다 작다면
        return sorted(nl) # 정렬된 nl을 반환
    pivot=sorted(random.sample(nl,3))[1] # 피봇에 nl에서 임의로 뽑은 3개의 값 중 중간값을 저장
    nl.remove(pivot) # nl에서 피봇 제거
    l=0 # 왼쪽좌표에 0
    r=len(nl)-1 # 오른쪽 좌표에 배열 마지막의 위치+1에서 -1을 뺀 값을 저장
    while l<=r: #왼쪽좌표가 오른쪽좌표보다 작은 동안 반복
        if not(nl[l]<pivot<nl[r]): # 만약 왼쪽좌표에 해당하는 nl의 값이 피봇보다 작은데 오른쪽좌표에 해당하는 nl의 값은 피봇보다 큰 경우가 아닌 경우
            if nl[l]<pivot:
                l+=1
                continue
            elif pivot<nl[r]:
                r-=1
                continue
            nl[l],nl[r]=nl[r],nl[l]
        l+=1
        r-=1
    if pivot < nl[l]:
        nl.insert(nl.index(nl[l]),pivot)
    return quick(nl[:l])+quick(nl[l:])


def quick(arr):
    if len(arr) < 3:
        return sorted(arr)
    else:
        left=1
        right=1
        pivots=random.sample(arr,3)
        pivots.remove(max(pivots))
        pivots.remove(min(pivots))
        pivot=pivots[0]
        arr.remove(pivot)
        arr.insert(0,pivot)
        while left+right<len(arr):
            l=arr[left]
            r=arr[-right]
            if l < pivot:
                if r < pivot:
                    left+=1
                else:
                    right+=1
            elif l > pivot:
                if r<pivot:
                    arr[left],arr[-right]=r,l
                    right+=1
                    left+=1
                else:
                    right+=1
        if arr[left] < pivot:
            arr[0],arr[left]=arr[left],pivot
        else:
            arr[0],arr[left-1]=arr[left-1],pivot
        if len(arr)!=3:
            return quick(arr[0:left])+quick(arr[left:len(arr)])
        else:
            return arr
