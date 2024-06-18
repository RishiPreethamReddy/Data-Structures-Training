graph={0:[(1,2)],1:[(0,2),(3,3),(2,4)],2:[(1,4)],3:[(2,3)]}
def dijkstras(start,n):
    visited=set()
    queue=[(start,0)]
    dist=[float('inf')]*(n)
    dist[start]=0
    visited.add(start)
    while queue:
        node,cost=queue.pop(0)
        for i in graph[node]:
            if i[0] not in visited:
                dist[i[0]]=min(dist[i[0]],cost+i[1])
                queue.append((i[0],dist[i[0]]))
                visited.add(i[0])
    print(dist)
dijkstras(0,4)