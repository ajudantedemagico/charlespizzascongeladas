from models.admin_model import listar_usuarios
from models.admin_model import deletar_usuario as deletar_usuario_model

def obter_usuarios_para_admin():
    usuarios = listar_usuarios()
    return usuarios

def deletar_usuario(usuario_id: int):
    deletar_usuario_model(usuario_id)
