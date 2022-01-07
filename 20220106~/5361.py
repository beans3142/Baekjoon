from sys import stdin
input=stdin.readline

price=[350.34,230.9,190.55,125.3,180.9]
t=int(input())
for i in range(t):
    parts=list(map(int,input().split()))
    total=0
    for no in range(5):
        total+=parts[no]*price[no]
    print(f"${total:.2f}")
