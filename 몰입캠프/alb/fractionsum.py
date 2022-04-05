from math import gcd
a,b=map(int,input().split())
c,d=map(int,input().split())
boonja=a*d+c*b
boonmo=b*d
GCD=gcd(boonja,boonmo)
print(boonja//GCD,boonmo//GCD)
