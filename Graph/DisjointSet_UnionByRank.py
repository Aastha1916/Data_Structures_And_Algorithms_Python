n = 7
edges = [[1,2],[2,3],[4,5],[6,7],[5,6]]
rank = [0]*(n+1)
parent = [i for i in range(n+1)]

#To find ultimate parent   
def find_Parent(node):
    if parent[node] == node:
        return node
    # Path Compression
    parent[node] = find_Parent(parent[node])
    return parent[node]

# To add edges
def UnionByRank(u,v):

    #Find Ultimate parent

    pu = find_Parent(u)
    pv = find_Parent(v)
    
    # Compare the ultimate Parents of both nodes

    if pu == pv:
        return 
    elif rank[pu] > rank[pv]:
        parent[pv] = pu
    elif rank[pv] > rank[pu]:
        parent[pu] = pv
    else:
        parent[pv] = pu
        rank[pu] += 1  
    
    #Adding the smaller ranked ultimate parent node to the higher ranked ultimate parent node

def findSet(u,v):
    #when the node and and parent of node are same --> same set
    if find_Parent(u) == find_Parent(v):
        return True
    #otherwise --> different set
    return False

for i in range(len(edges)):
    UnionByRank(edges[i][0], edges[i][1])

print(rank[1:])

if findSet(3, 4):
    print("Same Set")
else:
    print("Different Set")




