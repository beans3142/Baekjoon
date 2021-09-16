import sys
input=sys.stdin.readline
n,m=map(int,input().split())
b=sorted(list(map(int,input().split())))

def bt(idx,arr):
    queue=[[idx,arr]]
    while queue:
        i,l=queue.pop(0)
        if i == m+1:
            l=list(map(str,l))
            print(' '.join(l[1:]))
        else:
            for _ in b:
                if _ not in l:
                    queue.append([i+1,l+[_]])
        
    
bt(1,[0])
