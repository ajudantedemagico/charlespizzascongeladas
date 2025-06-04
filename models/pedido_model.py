from datetime import datetime
from database.db import conectar


def criar_pedido(id_usuario, total):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
        INSERT INTO pedido (id_usuario, data_pedido, status, total)
        VALUES (%s, %s, %s, %s)
        """
    dados = (id_usuario, datetime.now(), 'Em preparo', total)
    cursor.execute(sql, dados)
    conn.commit()

    id_pedido = cursor.lastrowid

    cursor.close()
    conn.close()

    return id_pedido


def adicionar_item_pedido(id_pedido, sabor, tamanho, quantidade, preco_unitario):
    conn = conectar()
    cursor = conn.cursor()

    subtotal = preco_unitario * quantidade

    sql = """
        INSERT INTO item_pedido (id_pedido, sabor, tamanho, quantidade, preco_unitario, subtotal)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
    dados = (id_pedido, sabor, tamanho, quantidade, preco_unitario, subtotal)
    cursor.execute(sql, dados)
    conn.commit()

    cursor.close()
    conn.close()


def listar_pedidos_por_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT * FROM pedido
        WHERE id_usuario = %s
        ORDER BY data_pedido DESC
        """
    cursor.execute(sql, (id_usuario,))
    pedidos = cursor.fetchall()

    cursor.close()
    conn.close()

    return pedidos


def listar_itens_do_pedido(id_pedido):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT * FROM item_pedido
        WHERE id_pedido = %s
        """
    cursor.execute(sql, (id_pedido,))
    itens = cursor.fetchall()

    cursor.close()
    conn.close()

    return itens


def alterar_status_pedido(id_pedido, novo_status):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
        UPDATE pedido
        SET status = %s
        WHERE id_pedido = %s
        """
    cursor.execute(sql, (novo_status, id_pedido))
    conn.commit()

    cursor.close()
    conn.close()