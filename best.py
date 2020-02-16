graph = {'S':[('A',3),('B',6),('C',5)],
'A':[('D',9),('E',8)],
'B':[('F',12),('G',14),('C',5)],
'C':[('H',7)],
'D':[],
'E':[],
'F':[],
'G':[],
'H':[('I',5),('J',6)],
'I':[('K',1),('L',10),('M',2)],
'J':[],
'K':[],
'L':[],
'M':[]
}


def bfs(graph, node, start):
  pq=[start]
  a=[]
  b=[]
  while(pq):
    u = pq.pop(0)
    if type(u) is tuple:
      u=u[0]
    b.append(u)
    if u == node:
      break
    else:
      for neigh in graph[u]:
        if neigh[0] not in b:
          pq.append(neigh)
          pq=sorted(pq, key=lambda x: x[1])
  for i,t in enumerate(a):
    if t is tuple:
      a[i]= t[0]
  return b
print(bfs(graph,'I','S'))