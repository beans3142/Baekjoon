from sys import stdin
input=stdin.readline
p2win=["R P","P S","S R"]

n=int(input())
for i in range(n):
    t=int(input())
    p1score=0
    p2score=0
    for j in range(t):
        case=input().rstrip()
        if case[0]==case[-1]:
            continue
        if case in p2win:
            p2score+=1
        else:
            p1score+=1
    if p1score==p2score:
        print("TIE")
    elif p1score<p2score:
        print("Player 2")
    else:
        print("Player 1")
