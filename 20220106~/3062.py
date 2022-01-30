from sys import stdin
input=stdin.readline

for i in range(int(input())):
    n=input()
    rev_n=n[::-1]
    lastn=int(n)+int(rev_n)
    if str(lastn)[::-1]==str(lastn):
        print('YES')
    else:
        print('NO')
