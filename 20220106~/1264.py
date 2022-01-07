from sys import stdin
input=stdin.readline

while True:
    l=input().rstrip()
    if l=="#":
        break
    cnt=0
    for i in l:
        if i in ["a","i","o","u","e","I","E","A","O","U"]:
            cnt+=1
    print(cnt)
