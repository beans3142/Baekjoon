from sys import stdin
input=stdin.readline

while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    if b-a==c-b:
        print("AP",2*c-b)
    else:
        print("GP",c**2//b)
    
# a,b,c 입력 자체가 등비 등차수열이다.
# 딱히 정렬해줄 필요 없음..

'''
TC

in
-1 -2 -3

out
-4

Wa - 입력 정렬해줘버린 경우.
0
'''
