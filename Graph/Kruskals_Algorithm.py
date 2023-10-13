# USING DISJOINT SET (UNION-FIND BY SIZE)

min_wt = 0
V = 9
parent = [i for i in range(V)]
size = [1 for _ in range(V)]
edges = [[0,1,4],[0,7,8],[1,2,8],[1,7,11],[2,3,7],[2,5,4],[2,8,2],[3,4,9],[3,5,14],[4,5,10],[5,6,2],[6,7,1],[6,8,6],[7,8,7]]


def find(parent,u):
    if parent[u] == u:
        return u
    parent[u] = find(parent,parent[u])
    return parent[u]

def union(parent,u,v,w):
    pu = find(parent,u)
    pv = find(parent,v)
    
    if pu == pv:
        return
    elif size[pu] < size[pv]:
        parent[pu] = pv
        size[pv] +=size[pu]
    else:
        parent[pv] = pu
        size[pu]+=size[pv]
    
edges.sort(key = lambda x:x[2])


for u,v,w in edges:
    if find(parent,u) != find(parent,v):
        min_wt +=w
        union(parent,u,v,w)

print(min_wt)
    