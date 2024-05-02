def insertar_ordenado(vector, numero):
    i = 0
    while i < len(vector) and vector[i] < numero:
        i += 1
    vector.insert(i, numero)

def buscar_numero(vector, numero):
    if numero in vector:
        return f"El número {numero} se encuentra en el vector."
    else:
        return f"El número {numero} no se encuentra en el vector."

def mostrar_vector(vector):
    print("Contenido del vector:")
    for numero in vector:
        print(numero)

N = int(input("Ingrese la cantidad de números a ingresar (no mayor a 100): "))
vector = []

for _ in range(N):
    numero = int(input("Ingrese un número entero: "))
    insertar_ordenado(vector, numero)

mostrar_vector(vector)

while True:
    numero_buscar = int(input("Ingrese un número para buscar en el vector (0 para salir): "))
    if numero_buscar == 0:
        break
    resultado = buscar_numero(vector, numero_buscar)
    print(resultado)