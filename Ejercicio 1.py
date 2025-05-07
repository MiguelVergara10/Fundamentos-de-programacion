# Solicitar al usuario un número entero


numero = int(input("Introduce un número entero: "))


if numero % 5 == 0:
        print("El numero si es divisible entre 5")

else:
    print("El numero no es divisible entre 5")


        
print("numeros desde 1 hasta", numero, ":")
for i in range(1, numero + 1):
    print(i, end= " ")