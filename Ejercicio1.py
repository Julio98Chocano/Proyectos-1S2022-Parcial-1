# Julio Chocano 201800684
# Programa elaborado el 24/02/22
# Juego simulado del gran 8, prueba

import random
import psycopg2

conn = psycopg2.connect("dbname='PrimerParcial' user='postgres' password='123'")
cur = conn.cursor()
insertar = 'INSERT INTO ejercicio1(dado1, dado2, suma, estado) VALUES(%s, %s, %s, %s)'

dado1 = 0
dado2 = 0
suma = 0

while suma != 8:
    print('Se procede a lanzar los dados')
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    print('Los valores obtenidos son:', dado1, 'y', dado2)
    if suma == 8:
        estado = 'Gano'
        cur.execute(insertar, (dado1, dado2, suma, estado))
        conn.commit()
    elif suma == 7:
        estado = 'Perdio'
        print('La suma es', suma, "y usted", estado)
        cur.execute(insertar, (dado1, dado2, suma, estado))
        conn.commit()
        break
    else:
        estado = 'No gano ni perdio'
        cur.execute(insertar, (dado1, dado2, suma, estado))
        conn.commit()
    print('La suma es', suma, "y usted", estado)



cur.close()
conn.close()