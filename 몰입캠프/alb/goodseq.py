from sys import stdin
input=stdin.readline

def check(w):
    for i in range(len(w)//2):
        able=False
        for j in range(i+1):
            if w[~j]!=w[~i+~j]:
                able=True
                break
        if not able:
            return able
    return True
    

def bt(w):
    if check(w)==False:
        return
    if len(w)==n:
        print(w)
        exit()
    bt(w+'1')
    bt(w+'2')
    bt(w+'3')

n=int(input())
bt('')

# 이게 단순 체크였다니..
