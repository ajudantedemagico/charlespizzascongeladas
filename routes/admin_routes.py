from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from controllers.admin_controller import obter_usuarios_para_admin, deletar_usuario

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/usuarios", response_class=HTMLResponse)
async def listar_usuarios_admin(request: Request):
    usuario = request.session.get("usuario")
    nome = usuario["nome"] if usuario else None

    if nome != "Administrador":
        return RedirectResponse(url="/login", status_code=303)

    usuarios = obter_usuarios_para_admin()

    return templates.TemplateResponse("admin.html", {
        "request": request,
        "usuarios": usuarios,
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
