train=[]
total=0

for i in range(0,9):
    out,get=map(int,input().split())
    total+=get-out
    train.append(total)

print(max(train))
