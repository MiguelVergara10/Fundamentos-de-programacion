# Pedir tres números al usuario
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))

# Guardar los números en una lista
numeros = [n1, n2, n3]

# Ordenar la lista de mayor a menor
numeros.sort(reverse=True)

# Mostrar los números ordenados
print("Números ordenados de mayor a menor:")
for numero in numeros:
    print(numero)