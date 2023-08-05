class bfs:

    def __init__(self,n,e,edge = [[1,2], [1,4], [2,3], [2, 5], [4, 5], [3, 5]]):
        self.n = n
        self.e = e
        self.edge = edge

    def traversal(self,src,graph):
        queue = [src]
        visited = [0]*(self.n+1)
        visited[src] = 1
        while queue:
            node = queue.pop(0)
            print(node,end=" ")
            for adj in graph[node] :
                if visited[adj] == 0:
                    queue.append(adj)
                    visited[adj] = 1
    
    def find_distance(self,src,graph):
        queue = [src]
        visited = [0]*(self.n+1)
        visited[src] = 1
        distance = [0]*(self.n+1)
        while queue:
            node = queue.pop(0)
            
            for adj in graph[node] :
                if visited[adj] == 0:
                    queue.append(adj)
                    visited[adj] = 1
                    distance[adj] += distance[node]+1
        return distance

    def undirected_adjList(self):
        adj_list = [[] for _ in range(self.n+1)]
        for u,v in self.edge:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list
    
    def directed_adjList(self):
        adj_list = [[] for _ in range(self.n+1)]
        for u,v in self.edge:
            adj_list[u].append(v)
        return adj_list

        
bfs_object = bfs(5,6)

# For directed graph:
directed_graph = bfs_object.directed_adjList()
print(directed_graph)
bfs_object.traversal(1,directed_graph)
directed_graph_distance = bfs_object.find_distance(1,directed_graph)
print("\n",directed_graph_distance[1:])

# For undirected graph:
undirected_graph = bfs_object.undirected_adjList()
print(undirected_graph)
bfs_object.traversal(1,undirected_graph)
undirected_graph_distance = bfs_object.find_distance(1,undirected_graph)
print("\n",undirected_graph_distance[1:])


        