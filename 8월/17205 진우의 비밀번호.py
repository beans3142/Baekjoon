import sys
input = sys.stdin.readline

n,m = map(int, input().split())
sites = {}

for i in range(n):
    site, password = input().rstrip().split()
    sites[site]=password

for i in range(m):
    print(sites[input().rstrip()])
