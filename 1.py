# Realizar un programa que lea los tiempos en los que de 10 corredores han acabado una carrera. El programa debe determinar qué corredores tienen el primer, segundo y último puesto, así como cuál es el tiempo medio en que se ha corrido la carrera.

tiempo = []
primer_puesto = 100
tiempo_primer = 0
ultimo_puesto = 0
segundo_puesto = 100
segundo_tiempo = 0
suma = 0
for j in range(0,10,1):
    print("Digite el tiempo del corredor", j+1)
    tiempo.append(int(input()))
    suma = tiempo[j]+suma

for i in range(0,10,1):
    if(tiempo[i]<primer_puesto):
        primer_puesto = tiempo[i]
        tiempo_primer = i
print("El corredor que obtuvo el primer puesto es el #: ", tiempo_primer+1)

for k in range(0,10,1):
    if(tiempo[k]>ultimo_puesto):
        ultimo_puesto = tiempo[k]
        ultimo_tiempo = k
print("El corredor que obtuvo el último puesto es el #: ", ultimo_tiempo+1)


for l in range(0,10,1):
    if((tiempo[l]<segundo_puesto) & (tiempo[tiempo_primer]!=tiempo[l])):
        segundo_puesto = tiempo[l]
        segundo_tiempo = l
print("El corredor que obtuvo el segundo puesto es el #: ", segundo_tiempo+1)

media = suma / 10
print("El tiempo promedio de la carrera es: ", media, "segundos")
