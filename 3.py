# Realiza un programa que pida al usuario N números enteros y los inserte de forma ordenada en un vector. (N será un valor que pediremos al principio, pero nunca deberá ser mayor de 100). El programa deberá permitir entonces la búsqueda de elementos dentro del vector mediante “búsqueda dicotómica”. Para ello (y mientras el usuario no decida salir) se pedirá el número que se desea saber si existe en el vector y se devolverá, en ese caso, su posición o se informará de que no existe. Para verificarlo, muestra el contenido del vector por pantalla.

N = int(input("Ingrese el valor de N: "))

if N > 100:
    print("N no puede ser mayor a100")
    exit()

vector = []

for i in range(N):
    num = int(input("Ingrese un numero entero: "))
    if len(vector) == 0:
        vector.append(num)
    else:
        for j in range(len(vector)):
            if num < vector[j]:
                vector.insert(j, num)
                break
            elif j == len(vector) - 1:
                vector.append(num)

print("Contenido del vector:", vector)

while True:
    buscar = int(input("Ingrese el numero que desea buscar (o ingrese 0 para salir): "))
    if buscar == 0:
        break

    inicio = 0
    fin = len(vector) - 1
    encontrado = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if vector[medio] == buscar:
            encontrado = True
            break
        elif vector[medio] < buscar:
            inicio = medio + 1
        else:
            fin = medio - 1

    if encontrado:
        print("El numero", buscar, "se encuentra en la posición", medio)
    else:
        print("El número", buscar, "no existe")