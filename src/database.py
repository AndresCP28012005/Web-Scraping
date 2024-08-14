import mysql.connector
from config import DB_CONFIG

def guardar_datos(productos):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), precio VARCHAR(255))")
    cursor.execute("DELETE FROM productos")
    
    for producto in productos:
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", producto)
    
    conn.commit()
    cursor.close()
    conn.close()
