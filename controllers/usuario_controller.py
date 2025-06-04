from models.usuario_model import Usuario
from fastapi import HTTPException


def cadastrar_usuario(usuario:Usuario):
    try:
        usuario.salvar()
    except Exception as e:
        print("erro ao cadastrar usuário:", e)
        raise HTTPException(status_code=500, detail="Erro interno ao criar usuário.")
    
def autenticar_usuario(email: str, senha: str):
    usuario = Usuario.autenticar(email, senha)
    return usuario

def autenticar_admin(email: str, senha: str):
    return email == "admin@gmail.com" and senha == "admin123"

def buscar_por_email(email: str):
    usuario = Usuario.buscar_por_email(email)
    return usuario

