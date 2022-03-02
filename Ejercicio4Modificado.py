# Julio Alejandro Chocano Lopez 201800684
# Elaborado el 24/02/22
# Programa que pide un numero y determina si es primo o compuesto
#Comentario nuevo

import psycopg2

conn = psycopg2.connect("dbname='PrimerParcial' user='postgres' password='123'")
cur = conn.cursor()
insertar = 'INSERT INTO ejercicio4(numero, primo_compuesto) VALUES(%s, %s)'

def identificar_num_primo(numero):
    if numero == 2:
        resultado = 'primo'
        return resultado
    for i in range(2, numero):
        if numero % i == 0:
            resultado = 'compuesto'
            return resultado
    resultado = 'primo'
    return resultado
        
num = int(input('Ingrese un numero: '))
       
respuesta = identificar_num_primo(num)

print('El numero es ' + respuesta)

cur.execute(insertar, (num, respuesta))
conn.commit()

cur.close()
conn.close()

