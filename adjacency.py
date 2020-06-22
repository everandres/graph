with open("adjacency.txt", "r") as f: #Abre y lee el txt extraido
    table = f.readlines()

table = list(map(lambda x: x.strip().split(";"), table)) #Convierte la información en una lista
table = table[1:]

input_nodes = [x[-2] for x in table]  #Selecciona la información dentro de la lista a trabajar
output_nodes = [x[-1] for x in table]

import numpy as np    #Biblioteca de Python que facilita la creación de matrices 
adjacency_matrix = np.zeros((759,759 ))


for input_node, output_node in zip(input_nodes, output_nodes): #Inicia ciclo 
       
    input_node = int(input_node.split(",")[0])
    output_node = int(output_node.split(",")[0])  
    #print(input_node, output_node)
    #print(input_node)
    adjacency_matrix[input_node, output_node] = 1 #Generación de la relación 1 si hay adyacencia

#print(input_node)


from collections import defaultdict
from pprint import pprint


graph = defaultdict(dict)
#print(graph)
edges = set()

for i, v in enumerate(adjacency_matrix, 1):
    for j, u in enumerate(v, 1):
        if u != 0 and frozenset([i, j]) not in edges:
            edges.add(frozenset([i, j]))
            graph[i].update({j: u})

for i in range(1, len(adjacency_matrix)+1):
    ("{}: {}".format(i, graph[i]))


#pprint(graph)

def BFS(graph, s):
    depth = {s: 0}
    frontier = [s]
    while len(frontier):
        current_node = frontier.pop(0)
        for neighbor in graph[current_node]:
            if neighbor not in depth:
                depth[neighbor] = depth[current_node] + 1
                frontier.append(neighbor)

    for node in graph:
        if node not in depth:
            depth[node] = -1

    return depth

for node in graph.keys():
    BFS(graph, node)
    (BFS(graph, node))

res = {node:BFS(graph, node) for node in graph.keys()}
#print(res)
import pandas as pd 
df = pd.DataFrame(res)
A = df.reindex(sorted(df))
Transpuesta = A.T 
print(Transpuesta)


array = A.values
nuevo = array.T
pprint(nuevo[95])

np.savetxt("distanciafinal.csv", nuevo, delimiter = ",", fmt="%.f") #Exportar información

Transpuesta.to_csv("fichero2.csv")