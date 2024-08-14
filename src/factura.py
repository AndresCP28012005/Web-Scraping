from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector
from config import DB_CONFIG
import os

def generar_factura(item, filename):
    # Asegurarse de que el directorio exista
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, f"Nombre: {item[0]}")
    c.drawString(100, 730, f"Precio: {item[1]}")
    
    # Agregar datos de toda la tabla
    c.drawString(100, 710, "Datos de la Tabla:")
    y = 690
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio FROM productos")
    
    for row in cursor.fetchall():
        c.drawString(100, y, f"Nombre: {row[0]}, Precio: {row[1]}")
        y -= 20
    
    cursor.close()
    conn.close()
    c.save()

