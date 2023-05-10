def bellman_ford(edges,n):
    if n==1:
        return 0
    weights = [float('inf') for _ in range(n) ] 
    weights[edges[0][0]] = 0

    for i in range(n-1):
        for u,v,edge_weight in edges:
            if weights[v] > edge_weight + weights[u]:
                weights[v] = edge_weight + weights[u]

    #To detect negative cycle
    for u,v,edge_weight in edges:
        if weights[v] > edge_weight + weights[u]:
            return 1
    return 0

n = 5
edges = [[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,1,1],[3,2,5],[4,3,-3]]
ans = bellman_ford(edges, n)
if ans:
    print("Negative cycle is present")
else:
    print("No negative cycle is present")
