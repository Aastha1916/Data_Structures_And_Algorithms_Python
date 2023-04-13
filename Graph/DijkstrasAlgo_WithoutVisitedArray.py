from heapq import *

edges = [[0,1,4],[0,3,5],[0,4,2],[1,2,4],[1,3,2],[2,3,2],[3,4,1]]
n = 5
graph = [[]for _ in range(len(edges))]
src = 0
dis = [float('inf')] * n
dis[src] = 0
pq = []
heappush(pq,(0,src))

for i in range(len(edges)):
    graph[edges[i][0]].append((edges[i][1],edges[i][2]))
    graph[edges[i][1]].append((edges[i][0],edges[i][2]))

while pq:
    curr_dis,curr_node = heappop(pq)
    for nbr in graph[curr_node]:
        new_dis = curr_dis + nbr[1]
        if new_dis < dis[nbr[0]] :
            heappush(pq,(new_dis,nbr[0]))
            dis[nbr[0]] = new_dis
                
print(dis)
                    