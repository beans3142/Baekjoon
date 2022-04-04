board=[input() for i in range(8)]

cnt=0

for i in range(8):
    for j in range(8):
        if i%2==0:
            if j%2==0:
                if board[i][j]=='F':
                    cnt+=1
        else:
            if j%2==1:
                if board[i][j]=='F':
                    cnt+=1

print(cnt)
