n= 5
e =6
source = 1
edge = [[1,2], [1,4], [2,3], [2, 5], [4, 5], [3, 5]]
adjlist = [[] for i in range(n+1)]
for i in range(e):
    adjlist[edge[i][0]].append(edge[i][1])
    adjlist[edge[i][1]].append(edge[i][0])

d = [0]*(n+1)
s = [0]*(n+1)
q = [source]
ans = [source]
s[source] = 1
while q:
    x = q.pop(0)
    l = adjlist[x]
    for i in l:
        if s[i] == 0:
            s[i] = 1
            d[i] = d[x] + 1
            q.append(i)
            ans.append(i)

print(d[1:])
print(ans)