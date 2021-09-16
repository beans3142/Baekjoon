# 다익스트라인 것 같음..?
# 플로이드/와샬로 각 지점 사이의 거리를 모두 구한 뒤 다익스트라를 진행(한개의 블럭으로 치고)
# 다익스트라를 진행할 경우 누적 거리값은 1/2해주고 모든 지점에서 목적지까지
# 플로이드 와샬을 통해 얻은 해당 위치에서 집까지 가는데 드는
# 비용과 다익스트라를 통해서 얻은 출발점에서 절반값으로 해당 위치까지
# 온 비용의 합을 매번 구해주며 최소값을 갱신해주면 될 듯? = 매우 어렵다..
from sys import maxsize
inf=maxsize
n=6
s=4
a=6
b=2
def solution(n,s,a,b,fares):
    mn=inf
    value_table=[[inf for i in range(n)]for _ in range(n)]

    for start,end,cost in fares:
        value_table[start-1][end-1]=min(value_table[start-1][end-1],cost)
        value_table[end-1][start-1]=min(value_table[end-1][start-1],cost)


    for i in range(n):
        value_table[i][i]=0
        for j in range(n):
            for k in range(n):
                value_table[j][k]=min(value_table[j][k],value_table[j][i]+value_table[i][k])

    for dest,start_cost in enumerate(value_table[s-1]):
        if start_cost!=inf:
            mn=min(mn,start_cost+value_table[dest][a-1]+value_table[dest][b-1])
        
    return mn 
