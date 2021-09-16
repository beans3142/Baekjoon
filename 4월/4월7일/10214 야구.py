
for i in range(int(input())):
    wl=ll=0
    for j in range(9):
        w,l=map(int,input().split())
        wl+=w
        ll+=l
    if wl != ll:
        if wl > ll:
            print('Yonsei')
        else:
            print('Korea')
    else:
        print('Draw')

#https://www.acmicpc.net/problem/10214
