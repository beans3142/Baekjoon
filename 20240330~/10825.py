[print(i[0]) for i in sorted([input().split() for i in range(int(input()))],key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))]
