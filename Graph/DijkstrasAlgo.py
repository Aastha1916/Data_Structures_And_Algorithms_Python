#TIME COMPLEXITY : O(V+ELOGV)
from heapq import *

edges = [[0,1,4],[0,3,5],[0,4,2],[1,2,4],[1,3,2],[2,3,2],[3,4,1]]
n = 5
graph = [[]for _ in range(len(edges))]
src = 0

for i in range(len(edges)):
    graph[edges[i][0]].append((edges[i][1],edges[i][2]))
    graph[edges[i][1]].append((edges[i][0],edges[i][2]))

def dijkstras(n,edges,src):
    minheap = []
    distance = [float('inf')] * n
    visited = [0] * n
    distance[src] = 0
    heappush(minheap,(distance[src],src))
    while minheap:
        currpair = heappop(minheap)
        currnode = currpair[1]
        currdistance = currpair[0]
        if visited[currnode] == 0 :
            visited[currnode] = 1
            for nbrpair in graph[currnode]:
                newdis = currdistance + nbrpair[1]
                if newdis < distance[nbrpair[0]]:
                    heappush(minheap,(newdis,nbrpair[0]))
                    distance[nbrpair[0]] = newdis
    return distance


ans = dijkstras(n,edges,src)
for i in ans:
    print(i,end = "-")
    
    