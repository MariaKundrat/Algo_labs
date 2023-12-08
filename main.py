from collections import defaultdict
from queue import Queue

def bfs(graph, start):    
    visited = set()
    queue = Queue()   
    queue.put(start)
    visited.add(start)    
    reachable_gas_storages = set()
    while not queue.empty():
        current_node = queue.get()
        for neighbor in graph.get(current_node, []):            
            if neighbor not in visited:
                visited.add(neighbor)                
                queue.put(neighbor)
                reachable_gas_storages.add(neighbor)
    return reachable_gas_storages

def accessible_gas_storages(pipelines, cities, gas_storages):
    graph_dic = defaultdict(list)
    result = defaultdict(list)

    for key, val in pipelines:        
        graph_dic[key].append(val)
    
    for gas_storage in gas_storages:
        reachable_cities = bfs(graph_dic, gas_storage)
        unreachable_cities = [city for city in cities if city not in reachable_cities]
        
        result[gas_storage] = unreachable_cities
    
    return result


with open("input.txt", "r", encoding="UTF-8") as f:    
    pipelines_file = eval(f.readline())
    cities_file = eval(f.readline())    
    gas_file = eval(f.readline())
is_reachable = accessible_gas_storages(pipelines_file, cities_file, gas_file)
print(is_reachable)

with open("result.txt", "w", encoding="UTF-8") as f:    
    for key, value in is_reachable.items():
        f.write(f"{key}:\n")        
        for city in value:
            f.write(f"\t{city}\n")      
