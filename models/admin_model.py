
from database.db import conectar  

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")  
    usuarios = cursor.fetchall() 
    conn.close()
    return usuarios

def deletar_usuario(usuario_id: int):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
        
# def listar_pedido():
#     conn = conectar()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM pedido")  
#     item_pedido = cursor.fetchall() 
#     conn.close()
#     return item_pedido

# def deletar_pedido(id_pedido: int):
#     conn = conectar()
#     cursor = conn.cursor()
#     try:
#         cursor.execute("DELETE FROM pedido WHERE id = %s", (id_pedido))
#         conn.commit()
#     finally:
#         cursor.close()
#         conn.close()