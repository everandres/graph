import csv 
with open("adjacency.csv", "r") as f: #Abrir la matriz de adyacencia
    prueba = list(csv.reader(f, delimiter=","))

print(prueba)

import numpy as np #importar la libreria Numpy
prueba = np.array(prueba[1:], dtype = np.int_)
prueba = np.delete(prueba, 0, axis=1)
A = prueba #Matriz de adyacencia
Z = np.ones((759)) #Matriz fila correspodiente al momento 0

final_matrix = np.empty((0, 759), int) #Matriz resultante


while sum(Z) != 0: #Loop para las iteraciones
    Z = np.dot(Z, A)
    final_matrix = np.vstack((final_matrix, Z))
    

print(final_matrix)
transpuesta = final_matrix.T #Matriz traspuesta
print(transpuesta)

np.savetxt("PF2.csv", transpuesta, delimiter = ",", fmt="%.f")