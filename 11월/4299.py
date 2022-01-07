a,b=map(int,input().split())
double_a=a+b
if double_a%2 or a<b:
    print(-1)
else:
    print(double_a//2,double_a//2-b)
