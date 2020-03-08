graph = {
    'A' : ['B','C','D'],
    'B' : ['C','F'],
    'C' : ['B''F'],
    'D' : ['G'],
    'E' : ['H'],
    'F' : [],
    'G' : ['D'],
    'H' :['E'],
	
}
    def __init__(self,vertices): 
    
        self.V = vertices 
        self.V = vertices 
        self.graph = defaultdict(list) 
  

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def DLS(self,src,target,maxDepth): 
  
        if src == target : return True
  
        if maxDepth <= 0 : return False
  
 
        for i in self.graph[src]: 
                if(self.DLS(i,target,maxDepth-1)): 
                    return True
        return False
