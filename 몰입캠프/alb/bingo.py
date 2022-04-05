arr=[[*map(int,input().split())]for i in range(5)]
hesaid=[[*map(int,input().split())]for i in range(5)]
def checkBingo():
    totalbingo=0
    for i in range(5):
        isBingo=True
        for j in range(5):
            if arr[i][j]!=-1:
                isBingo=False
                break
        if isBingo:
            totalbingo+=1

    for i in range(5):
        isBingo=True
        for j in range(5):
            if arr[j][i]!=-1:
                isBingo=False
                break
        if isBingo:
            totalbingo+=1

    isBingo=True
    for i in range(5):
        if arr[i][i]!=-1:
            isBingo=False
            break
    if isBingo:
        totalbingo+=1
    isBingo=True
    for i in range(5):
        if arr[~i][i]!=-1:
            isBingo=False
            break
    if isBingo:
        totalbingo+=1
    if totalbingo>=3:
        return True
    return False

def fill(x):
    global arr
    for i in range(5):
        for j in range(5):
            if arr[i][j]==x:
                arr[i][j]=-1

turn=0
for i in range(5):
    for j in range(5):
        fill(hesaid[i][j])
        turn+=1
        if turn>=5:
            if checkBingo():
                print(turn)
                exit()
