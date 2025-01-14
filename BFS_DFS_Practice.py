# BFS in Python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
v = [] # visited
q = [] # queue
def bfs(v, graph, node):
    v.append(node)
    q.append(node)
    while q:
        m = q.pop(0)
        print(m.node, end=", ")
        for i in graph[m]:
            if i not in v:
                v.append(i)
                q.append(i)
            

# bfs(v, graph, '5')



# DFS in Python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
v = set() # visited
def dfs(v, graph, node):
    if node not in v:
        print(node, end=", ") 
        v.add(node)
    for i in graph[node]:
        dfs(v, graph, i) # recursive