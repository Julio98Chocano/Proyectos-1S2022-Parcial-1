# Julio Chocano 201800684
# Programa elaborado el 24/02/22
# Calculadora de iva de un precio
#COmentario nuevo

import psycopg2

conn = psycopg2.connect("dbname='PrimerParcial' user='postgres' password='123'")
cur = conn.cursor()
insertar = 'INSERT INTO ejercicio3(precio, iva, precio_original) VALUES(%s, %s, %s)'

precio = float(input('Ingrese un precio: '))

iva = 0.12*precio
precio_original = precio - iva

print('El iva es:', iva)
print('El precio original es:', precio_original)

cur.execute(insertar, (precio, iva, precio_original))
conn.commit()

cur.close()
conn.close()
