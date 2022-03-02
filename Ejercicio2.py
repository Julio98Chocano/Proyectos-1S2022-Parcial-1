# Julio Chocano 201800684
# Programa elaborado el 24/02/22
# Calculadora estadistica de calificaciones.

import statistics
import psycopg2

conn = psycopg2.connect("dbname='PrimerParcial' user='postgres' password='123'")
cur = conn.cursor()
insertar = 'INSERT INTO ejercicio2(calificaciones, media, mediana, moda, desv_estandar, varianza, rango) VALUES(%s, %s, %s, %s, %s, %s, %s)'

calificaciones = []
for i in range(5):
    calificacion = int(input('Ingrese sus calificaciones:'))
    calificaciones.append(calificacion)

media = statistics.mean(calificaciones)
mediana = statistics.median(calificaciones)
moda = statistics.mode(calificaciones)
desviacion_estandar = statistics.pstdev(calificaciones)
varianza = statistics.pvariance(calificaciones)

maximo = max(calificaciones)
minimo = min(calificaciones)
rango = maximo - minimo

print('\nLa media es:', media)
print('La mediana es:', mediana)
print('La moda es:', moda)
print('La desviacion estandar es:', desviacion_estandar)
print('La varianza es:', varianza)
print('El rango es:', rango)

cur.execute(insertar, (calificaciones, media, mediana, moda, desviacion_estandar, varianza, rango))
conn.commit()

cur.close()
conn.close()