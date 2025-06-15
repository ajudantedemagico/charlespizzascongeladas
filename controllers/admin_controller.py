from models.admin_model import (
    listar_usuarios,
    deletar_usuario as deletar_usuario_model,
    listar_todos_pedidos,
    buscar_pedidos_por_usuario,
    alterar_status_pedido
)

def obter_usuarios_para_admin():
    usuarios = listar_usuarios()
    return usuarios

def deletar_usuario(usuario_id: int):
    deletar_usuario_model(usuario_id)

def obter_todos_pedidos():
    return listar_todos_pedidos()

def obter_pedidos_por_usuario(usuario_id: int):
    return buscar_pedidos_por_usuario(usuario_id)

def atualizar_status_pedido(pedido_id: int, novo_status: str):
    alterar_status_pedido(pedido_id, novo_status)