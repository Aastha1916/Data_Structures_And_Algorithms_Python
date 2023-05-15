''' A directed graph is strongly connected if there is a path between all pairs of vertices.
A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph.'''

adj1 = [[2,3],[0],[1],[4],[]]
V = 5

visited1 = [0]*V
visited2 = [0]*V
stack1 = []
stack2 = []

def dfs(node,stack,visited,adj):
    visited[node] = 1
    for u in adj[node]:
        if visited[u] == 0:
            dfs(u,stack,visited,adj)
    stack.append(node)

#PATH 1    
for i in range(V):
    if visited1[i] == 0 :
        dfs(i,stack1,visited1,adj1)

adj_rev = [[] for _ in range(len(adj1))]
for u in range(V):
    for v in adj1[u] :
        adj_rev[v].append(u)
    
ans = 0
#PATH 2
while stack1:
    x = stack1.pop()
    if visited2[x] == 0:
        dfs(x,stack2,visited2,adj_rev)
        ans += 1
print(ans)
    

