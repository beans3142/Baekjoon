n,s=map(int,input().split())
print(sum([str(i+1).count(str(s)) for i in range(n)]))
