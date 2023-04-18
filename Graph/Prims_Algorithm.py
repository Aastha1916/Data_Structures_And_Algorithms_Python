from heapq import *

edges = [[0,1,4],[0,7,8],[1,2,8],[1,7,11],[2,3,7],[2,5,4],[2,8,2],[3,4,9],[3,5,14],[4,5,10],[5,6,2],[6,7,1],[6,8,6],[7,8,7]]
n = 9
graph = [[]for _ in range(len(edges))]
queue = []   #Priority queue for storing edges in ascending order of their weight
parent = [0]*n
MSTSet = [False]*n
distance = [float('inf')]*n

for i in range(len(edges)):
    graph[edges[i][0]].append((edges[i][1],edges[i][2]))
    graph[edges[i][1]].append((edges[i][0],edges[i][2]))

def PrimsAlgo(n,edges,queue,MSTSet,parent,distance):
    distance[0] = 0
    parent[0] = -1
    heappush(queue,(0,0))
    while queue:
        currpair = heappop(queue)

        currnode = currpair[1] #Node
        currdistance = currpair[0] #Distance

        if MSTSet[currnode] == False :
            MSTSet[currnode] = True
            for nbrpair in graph[currnode]:
                if nbrpair[1] < distance[nbrpair[0]] and MSTSet[nbrpair[0]]==False:
                    heappush(queue,(nbrpair[1],nbrpair[0]))
                    distance[nbrpair[0]] = nbrpair[1]
                    parent[nbrpair[0]] = currnode

PrimsAlgo(n,edges,queue,MSTSet,parent,distance)
print(sum(distance))
    
    