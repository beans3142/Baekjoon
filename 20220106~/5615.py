from sys import stdin
input=stdin.readline

base={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,61,67}

def mrt(n,b,s,t):
	x=pow(b,t,n)
	if x==1 or x==n-1:
		return 1
	else:
		for i in range(s):
			if x==n-1:
				return 1
			x=pow(x,2,n)
		return 0

def isp(n):
	if n in base:
		return True
	if n<2 or n%2==0:
		return False
	s=0
	t=n-1
	while t%2==0:
		s+=1
		t//=2
	
	for i in base:
		if not mrt(n,i,s,t):
			return False
	return True

ans=0
for i in range(int(input())):
	ans+=isp(int(input())*2+1)
print(ans)
