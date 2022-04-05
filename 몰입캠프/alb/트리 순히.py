from collections import defaultdict
from sys import stdin
input=stdin.readline

n=int(input())
tree=defaultdict(list)
preorder=[]
inorder=[]
postorder=[]

for i in range(n):
    node,nodeLeft,nodeRight=map(int,input().split())
    tree[node]=[nodeLeft,nodeRight]

def traversal(node):
    if node==-1: # 현재 노드가 -1이면 (끝)
        return #종료
    
    nodeLeft=tree[node][0] # 좌측노드
    nodeRight=tree[node][1] # 우측노드
    
    preorder.append(node)
    
    traversal(nodeLeft) # 왼쪽 노드로 탐색
    
    inorder.append(node)
    
    traversal(nodeRight) # 오른쪽 노드로 탐색
    
    postorder.append(node)

traversal(0)

print(*preorder)
print(*inorder)
print(*postorder)
