# Dados dos vectores tridimensionales {(a1, a2, a3) y (b1, b2, b3)}, calcular su producto escalar y su producto vectorial mediante:
# Producto vectorial de dos vectores u(x,y,z) y v(x,y,z), obteniendo: w(x,y,z)
# w[x] = u[y] * v[z] - u[z] * v[y];
# w[y] = u[z] * v[x] - u[x] * v[z];
# w[z] = u[x] * v[y] - u[y] * v[x];

a1 = int(input("Ingrese el valor de a1: "))
a2 = int(input("Ingrese el valor de a2: "))
a3 = int(input("Ingrese el valor de a3: "))

b1 = int(input("Ingrese el valor de b1: "))
b2 = int(input("Ingrese el valor de b2: "))
b3 = int(input("Ingrese el valor de b3: "))

a = (a1, a2, a3)
b = (b1, b2, b3)

producto_escalar = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

producto_vectorial = [
    a[1] * b[2] - a[2] * b[1],
    a[2] * b[0] - a[0] * b[2],
    a[0] * b[1] - a[1] * b[0]
]

print("producto escalar:", producto_escalar)
print("producto vectorial:", producto_vectorial)


