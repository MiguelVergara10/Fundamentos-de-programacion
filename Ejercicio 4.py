# Pedir al usuario dos números
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

# Comparar los dos números y mostrar el resultado
if n1 == n2:
    print("Los dos números son iguales.")
elif n1 < n2:
    print(f"El primer número ({n1}) es menor que el segundo número ({n2}).")
else:
    print(f"El primer número ({n1}) es mayor que el segundo número ({n2}).")