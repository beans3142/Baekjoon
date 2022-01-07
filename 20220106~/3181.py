from sys import stdin
input=stdin.readline

div=['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

s=input().rstrip().split()

ns=s[0][0].upper()+''.join([i[0].upper() for i in s[1:] if i not in div])
print(ns)
