# Pedir al usuario que ingrese dos números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

# Verificar si uno es múltiplo del otro
if n1 % n2 == 0:
    print(f"{n1} es múltiplo de {n2}.")
elif n2 % n1 == 0:
    print(f"{n2} es múltiplo de {n1}.")
else:
    print("Ninguno de los dos números es múltiplo del otro.")