from sys import stdin
input=stdin.readline

sik,ans=input().rstrip().split('=')
result=eval(sik)
if int(ans)==result:
    print("YES")
else:
    print("NO")
