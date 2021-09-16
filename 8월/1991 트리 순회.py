from sys import stdin
input=stdin.readline

n=int(input())
tree={chr(65+i):[0,0,0]for i in range(n)}

for i in range(n):
    root,left,right=input().rstrip().split()
    tree[root][0]=left
    tree[root][1]=right

preorder=[]
inorder=[]
postorder=[]

def trav(x):
    preorder.append(x)
    if tree[x][0]!='.':
        trav(tree[x][0])
    inorder.append(x)
    if tree[x][1]!='.':
        trav(tree[x][1])
    postorder.append(x)        


trav('A')

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
