from sys import stdin
input=stdin.readline

while True:
    try:
        n=int(input())
        p=1
        while True:
            p*=9
            if p>=n:
                print("Baekjoon wins.")
                break
            p*=2
            if p>=n:
                print("Donghyuk wins.")
                break
    except:
        break
