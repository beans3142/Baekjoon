from sys import stdin
input=stdin.readline
s,k,h=map(int,input().split())
univ={s:"Soongsil",k:"Korea",h:"Hanyang"}
if s+k+h>=100:
    print("OK")
else:
    print(univ[min(s,k,h)])
