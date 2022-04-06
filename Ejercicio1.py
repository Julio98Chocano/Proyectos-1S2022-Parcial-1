# Julio Chocano 201800684
# Creado: 24/02/2022
# Ultima modificacion: 05/04/2022
# Juego simulado del gran 8

# Julio Chocano 201800684
# Creado: 24/02/2022
# Ultima modificacion: 05/04/2022
# Juego simulado del gran 8

import random
import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()

try: 
    connection = psycopg2.connect(user=os.environ.get("pg_usuario"),
                                password=os.environ.get("pg_password"),
                                database=os.environ.get("pg_base_de_datos"))
    cursor = connection.cursor()
except (Exception, psycopg2.Error) as error:
    print('Error al conectar a postgres', error)
    quit()

insertar = 'INSERT INTO ejercicio1(dado1, dado2, suma, estado) VALUES(%s, %s, %s, %s)'

menu = {}
menu['1'] = 'Iniciar juego.' 
menu['2'] = 'Ver historial.'
menu['3'] = 'Borrar historial.'
menu['4'] = 'Salir.'

while True: 
    options=menu.keys()
    for entry in options: 
        print(entry, menu[entry])
    selection = input("\nIngrese el numero de la opcion que desea: ") 
    if selection =='1': 
        suma = 0
        while suma != 8:
            print('Se procede a lanzar los dados')
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            suma = dado1 + dado2
            print('Los valores obtenidos son:', dado1, 'y', dado2)
            if suma == 8:
                estado = 'Gano'
                valores = (dado1, dado2, suma, estado)
                cursor.execute(insertar, valores)
                connection.commit()
            elif suma == 7:
                estado = 'Perdio'
                valores = (dado1, dado2, suma, estado)
                cursor.execute(insertar, valores)
                connection.commit()
            else:
                estado = 'No gano ni perdio'
                valores = (dado1, dado2, suma, estado)
                cursor.execute(insertar, valores)
                connection.commit()
            print(f'La suma es {suma} y usted {estado}\n')
    elif selection == '2': 
        cursor.execute('SELECT * from Ejercicio1')
        historial = cursor.fetchall()
        print('Historial:', historial)
    elif selection == '3':
        cursor.execute('DELETE from Ejercicio1')
        print('Se ha borrado el historial.')
    elif selection == '4':
        break
    else: 
        print('No ingreso una opcion valida.')


cursor.close()
connection.close()