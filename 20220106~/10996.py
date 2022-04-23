n=int(input())

for i in range(n*2):
    print((("* " if i%2==0 else " *")*n)[:n])
