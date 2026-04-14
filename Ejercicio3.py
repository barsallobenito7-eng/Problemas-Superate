
numeros = []

print("Introduce los números ganadores de la lotería primitiva:")

for i in range(6):  
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)

# Ordenar la lista de menor a mayor
numeros.sort()

# Mostrar el resultado
print("Números ordenados de menor a mayor:")
print(numeros)