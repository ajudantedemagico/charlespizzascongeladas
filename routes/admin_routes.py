from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from controllers.admin_controller import (
    obter_usuarios_para_admin,
    deletar_usuario,
    obter_todos_pedidos,
    obter_pedidos_por_usuario,
    atualizar_status_pedido
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/usuarios", response_class=HTMLResponse)
async def listar_usuarios_admin(request: Request):
    usuario = request.session.get("usuario")
    nome = usuario["nome"] if usuario else None

    if nome != "Administrador":
        return RedirectResponse(url="/login", status_code=303)

    usuarios = obter_usuarios_para_admin()
    pedidos = obter_todos_pedidos()  # agora também busca os pedidos

    return templates.TemplateResponse("admin.html", {
        "request": request,
        "usuarios": usuarios,
        "pedidos": pedidos,
        "nome": nome
    })


@router.post("/admin/usuarios/excluir/{usuario_id}")
async def excluir_usuario(usuario_id: int, request: Request):
    usuario = request.session.get("usuario")
    nome = usuario["nome"] if usuario else None

    if nome != "Administrador":
        return RedirectResponse(url="/login", status_code=303)

    deletar_usuario(usuario_id)
    return RedirectResponse(url="/admin/usuarios", status_code=303)


@router.get("/admin/pedidos", response_class=HTMLResponse)
async def listar_todos_pedidos(request: Request):
    usuario = request.session.get("usuario")
    nome = usuario["nome"] if usuario else None

    if nome != "Administrador":
        return RedirectResponse(url="/login", status_code=303)
    
    usuarios = obter_usuarios_para_admin()
    pedidos = obter_todos_pedidos()
    
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "usuarios": usuarios,
        "pedidos": pedidos,
        "nome": nome
    })


@router.post("/admin/pedidos/por-usuario")
async def buscar_pedidos_usuario(request: Request, usuario_id: int = Form(...)):
    usuario = request.session.get("usuario")
    nome = usuario["nome"] if usuario else None

    if nome != "Administrador":
        return RedirectResponse(url="/login", status_code=303)
    
    usuarios = obter_usuarios_para_admin()
    pedidos = obter_pedidos_por_usuario(usuario_id)
    
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "usuarios": usuarios,
        "pedidos": pedidos,
        "nome": nome
    })


@router.post("/admin/pedidos/alterar-status")
async def alterar_status(request: Request, pedido_id: int = Form(...), novo_status: str = Form(...)):
    usuario = request.session.get("usuario")
    nome = usuario["nome"] if usuario else None

    if nome != "Administrador":
        return RedirectResponse(url="/login", status_code=303)

    atualizar_status_pedido(pedido_id, novo_status)
    return RedirectResponse(url="/admin/usuarios", status_code=303)
