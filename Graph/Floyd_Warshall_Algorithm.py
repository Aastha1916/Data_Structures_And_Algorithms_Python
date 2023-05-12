# To find the shortest path between all the pairs of vertices in a weighted graph
def shortest_distance(matrix):
    n = len(matrix)

    for row in range(n):
		    for col in range(n):
		        if matrix[row][col] == -1:
		            matrix[row][col] = 1001

    for via in range(n):
        for src in range(n):
            for des in range(n):
                matrix[src][des] = min(matrix[src][des],matrix[src][via]+matrix[via][des])
    
    for row in range(n):
		    for col in range(n):
		        if matrix[row][col] == 1001:
		            matrix[row][col] = -1
    

matrix = [[0,1,43],[1,0,6],[-1,-1,0]]
shortest_distance(matrix)
print(matrix)

#OUTPUT:{{0,1,7},{1,0,6},{-1,-1,0}}