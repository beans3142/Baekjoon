from sys import setrecursionlimit
setrecursionlimit(1000000)

N ,start =  list(map(int,input().split()))

count = [False for x in range(N+1) ]
def recursive(start):
    global count 
        
    if start > N  :
        return
    if count[start] == True:
        return
    
    count[start] = True
    
    
    recursive(start*2)
    if start not in [1,2]:
        recursive(start//3)
    else:
        return
    
recursive(start)
print(N- sum(count))
