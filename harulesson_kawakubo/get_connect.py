import mysql.connector

def get_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="harulesson_kawakubo"
    )
    