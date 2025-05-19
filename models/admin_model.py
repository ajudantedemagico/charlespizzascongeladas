
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



