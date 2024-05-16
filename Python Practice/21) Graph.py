class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    
    def get_paths(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths
        
    def get_shortest_path(self,start,end,path=[]):
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = self.get_paths(start, end, path)
        minv = 1000    
        for p in paths:
            if minv > len(p):
                minv = len(p)
                ans = [p]
            elif minv == len(p):
                ans.append(p)
        return ans
        
        
routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

route_graph = Graph(routes)

start = "Mumbai"
end = "New York"

print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))