def dfs(node,graph,visited,ans):
    ans.append(node)
    visited[node] = 1
    for neigbour in graph[node]:
        if visited[neigbour] == 0:
            dfs(neigbour, graph, visited, ans)

n= 7
e = 7
source = 1
edge = [[1,2], [1,4], [2,3], [2, 5], [4, 5], [3, 5],[6,7]]
adjlist = [[] for i in range(n+1)]
for i in range(e):
    adjlist[edge[i][0]].append(edge[i][1])
    adjlist[edge[i][1]].append(edge[i][0])

visited = [0] * (n+1)
ans = []
result = []
dfs(1,adjlist,visited,ans)
result.append(ans)
for i in range(1,n+1):
    if visited[i] == 0:
        ans = []
        dfs(i,adjlist,visited,ans)
        result.append(ans)

print(result)



