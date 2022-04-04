import sys

input=sys.stdin.readline

cnt=0
end=False

while True:
    cnt+=1
    lines=[]
    while True:
        line=list(map(int,input().split()))
        lines+=line
        try:
            if line[-1]==0 and line[-2]==0:
                arr=lines[:-2]
                break
            elif line[-1]<0 and line[-2]<0:
                end=True
                break
        except:
            pass
    if end:
        break
    back_tree={}
    tree={}
    visited={}
    is_tree=True
    root=0
    if not arr:
        print(f'Case {cnt} is a tree.')
        continue
    for _ in arr:
        visited[_]=0
    for _ in range(len(arr)):
        back_tree[arr[_]]=[]
        tree[arr[_]]=[]
    for _ in range(0,len(arr),2):
        tree[arr[_]].append(arr[_+1])
        back_tree[arr[_+1]].append(arr[_])
    for _ in back_tree:
        if len(back_tree[_])>1: # 2번 조건
            is_tree=False
            break
        if len(back_tree[_])==0: # 3번 조건
            if root!=0:
                is_tree=False
                break
            root=_
    if is_tree:
        if root==0: #1번 조건
            is_tree=False
        else:
            visited[root]=1
        for _ in back_tree:
            n=_
            while back_tree[n] and visited[n]==0:
                visited[n]=1
                n=back_tree[n][0]
        for _ in visited:
            if visited[_]==0:
                is_tree=False
                break
    if is_tree:
        print(f'Case {cnt} is a tree.')
        continue
    print(f'Case {cnt} is not a tree.')
