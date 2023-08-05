class dfs:

    def __init__(self,n,e,edge = [[1,2], [1,4], [2,3], [2, 5], [4, 5], [3, 5]]):
        self.n = n
        self.e = e
        self.edge = edge
        self.visited = [0]*(n+1)

    def recursive_traversal(self,src,graph,visited):
        visited[src] = 1

        for adj in graph[src]:
            if visited[adj] == 0:
                self.recursive_traversal(adj,graph,visited)


    def iterative_traversal(self,src,graph):
        visited = [0]*(self.n+1)
        stack = [src]
        visited[src] = 1
        while stack:
            node = stack.pop()
            print(node,end = " ")
            for adj in graph[node]:
                if visited[adj] == 0:
                    stack.append(adj)
                    visited[adj] = 1

    
    def find_distance(self,src,graph):
        visited = [0]*(self.n+1)
        distance = [0]*(self.n+1)
        stack = [src]
        visited[src] = 1
        while stack:
            node = stack.pop()
            for adj in graph[node]:
                if visited[adj] == 0:
                    stack.append(adj)
                    visited[adj] = 1
                    distance[adj] += distance[adj]+1
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

        
dfs_object = dfs(5,6)

# For directed graph:
directed_graph = dfs_object.directed_adjList()
print(directed_graph)
dfs_object.recursive_traversal(1,directed_graph,dfs_object.visited)
dfs_object.iterative_traversal(1,directed_graph)
directed_graph_distance = dfs_object.find_distance(1,directed_graph)
print("\n",directed_graph_distance[1:])

# For undirected graph:
undirected_graph = dfs_object.undirected_adjList()
print(undirected_graph)
dfs_object.recursive_traversal(1,undirected_graph,dfs_object.visited)
dfs_object.iterative_traversal(1,undirected_graph)
undirected_graph_distance = dfs_object.find_distance(1,undirected_graph)
print("\n",undirected_graph_distance[1:])


        



