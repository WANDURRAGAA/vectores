#Realiza un programa que vaya pidiendo números enteros mientras que no se introduzca el cero y rellene dos vectores, uno con los números pares, y otro con los números impares. Al final, se debe mostrar por pantalla tanto el vector de números pares como el de impares.

pares = []
impares = []

while True:
    n_entero = int(input("Digite un numero entero: "))
    if n_entero == 0:
        break
    if n_entero % 2 == 0:
        pares.append(n_entero)
    else:
        impares.append(n_entero)

print("Números pares: ", pares)
print("Números impares: ", impares)

