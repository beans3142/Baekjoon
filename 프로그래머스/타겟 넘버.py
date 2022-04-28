arr=[]
tar=0

def bt(s,idx):
    if idx==len(arr):
        if s==tar:
            return 1
        return 0
    return bt(s+arr[idx],idx+1)+bt(s-arr[idx],idx+1)    
    

def solution(numbers, target):
    global arr,tar
    arr=numbers
    tar=target
    answer = bt(0,0)
    return answer
