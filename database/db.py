import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="arthur",
        database="charles_pizzaria"
    )