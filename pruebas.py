# Creado: 05/04/2022
# Ultima modificacion: 05/04/2022
# Hola
import random
import psycopg2

conn = psycopg2.connect("dbname='PrimerParcial' user='postgres' password='123'")
cur = conn.cursor()

cur.close()
conn.close()