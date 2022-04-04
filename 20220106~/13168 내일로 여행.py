from sys import stdin,maxsize
from collections import defaultdict
inf=maxsize
input=stdin.readline
n,r=map(int,input().split())
type_dict={"Subway":1,"Bus":1,"Taxi":1,"Airplane":1,"KTX":1,"S-Train":0.5,\
           "V-Train":0.5,"ITX-Saemaeul":0,"ITX-Cheongchun":0,"Mugunghwa":0}
city=defaultdict(int)
route=[[inf for i in range(n+1)]for i in range(n+1)]
route_r=[[inf for i in range(n+1)]for i in range(n+1)]
citys=input().rstrip().split()
for i,name in enumerate(citys):
    if city[name]:
        continue
    city[name]=i+1

num_to_visit=int(input())
to_visit=input().rstrip().split()

num_of_way=int(input())

for i in range(num_of_way):
    typ,city1,city2,price=input().rstrip().split()
    price=int(price)
    route[city[city1]][city[city2]]=route[city[city2]][city[city1]]=min(price,route[city[city2]][city[city1]])
    route_r[city[city1]][city[city2]]=route_r[city[city2]][city[city1]]=min(route_r[city[city2]][city[city1]],price*type_dict[typ])


for i in range(1,n+1):
    route_r[i][i]=0
    route[i][i]=0
    for j in range(1,n+1):
        for k in range(1,n+1):
            route[j][k]=min(route[j][k],route[j][i]+route[i][k])
            route_r[j][k]=min(route_r[j][k],route_r[j][i]+route_r[i][k])

without_r=0
for i in range(1,num_to_visit):
    without_r+=route[city[to_visit[i-1]]][city[to_visit[i]]]

with_r=r
for i in range(1,num_to_visit):
    with_r+=route_r[city[to_visit[i-1]]][city[to_visit[i]]]

if with_r<without_r:
    print('Yes')
else:
    print('No')
