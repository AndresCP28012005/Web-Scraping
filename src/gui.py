import tkinter as tk
from tkinter import ttk, messagebox
from scraper import recolectar_datos
from database import guardar_datos
from factura import generar_factura
import mysql.connector
from config import DB_CONFIG

def cargar_datos(tree):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, precio FROM productos")
    
    for row in tree.get_children():
        tree.delete(row)

    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)
    
    cursor.close()
    conn.close()

def recolectar_y_guardar_datos(tree):
    productos = recolectar_datos()
    guardar_datos(productos)
    cargar_datos(tree)

def generar_factura_de_fila(tree):
    selected_item = tree.selection()
    if selected_item:
        item_id = tree.item(selected_item[0])['values'][0]
        item = (tree.item(selected_item[0])['values'][1], tree.item(selected_item[0])['values'][2])
        filename = f"data/factura_{item_id}.pdf"
        generar_factura(item, filename)
        messagebox.showinfo("Factura", f"Factura generada como '{filename}'.")
    else:
        messagebox.showwarning("Seleccionar fila", "Por favor, selecciona una fila.")

def crear_interfaz():
    root = tk.Tk()
    root.title("Recoleccion de Datos")

    # Crear tabla
    tree = ttk.Treeview(root, columns=("id", "nombre", "precio"), show='headings')
    tree.heading("id", text="ID")
    tree.heading("nombre", text="Nombre")
    tree.heading("precio", text="Precio")
    tree.pack()

    # Boton para recolectar datos
    btn_recolectar = tk.Button(root, text="Recolectar datos", command=lambda: recolectar_y_guardar_datos(tree))
    btn_recolectar.pack()

    # Boton para generar factura
    btn_factura = tk.Button(root, text="Generar Factura", command=lambda: generar_factura_de_fila(tree))
    btn_factura.pack()

    root.mainloop()
