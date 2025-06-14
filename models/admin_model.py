
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
        
def listar_todos_pedidos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            p.id_pedido, p.data_pedido, p.status, p.total, p.data_entrega,
            p.cupom, p.desconto, p.valor_final,
            u.id AS id_usuario, u.nome, u.email
        FROM pedido p
        JOIN usuarios u ON p.id_usuario = u.id
        ORDER BY p.data_pedido DESC                               
    """)
    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

def buscar_pedidos_por_usuario(usuario_id: int):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            p.id_pedido, p.data_pedido, p.status, p.total, p.data_entrega,
            p.cupom, p.desconto, p.valor_final,
            u.id AS id_usuario, u.nome, u.email
        FROM pedido p
        JOIN usuarios u ON p.id_usuario = u.id
        WHERE p.id_usuario = %s
        ORDER BY p.data_pedido DESC                     
    """, (usuario_id,))
    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

def alterar_status_pedido(pedido_id: int, novo_status: str):
    conn = conectar()
    cursor = conn.cursor()
    try: 
        cursor.execute("""
            UPDATE pedido
            SET status = %s
            WHERE id_pedido = %s
    """, (novo_status, pedido_id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()