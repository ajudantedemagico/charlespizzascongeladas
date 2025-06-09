from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from controllers import pedido_controller, usuario_controller
from models import pedido_model 
from controllers.pedido_controller import pegar_usuario_logado
from fastapi.templating import Jinja2Templates
from typing import List
from datetime import datetime

templates = Jinja2Templates(directory="templates")

def datetimeformat(value, format="%d/%m/%Y"):
    if isinstance(value, datetime):
        return value.strftime(format)
    return value
templates.env.filters["datetimeformat"] = datetimeformat

router = APIRouter(
    prefix="",
    tags=["Pedidos"]
)


@router.get("/meus-pedidos", response_class=HTMLResponse)
def meus_pedidos(request: Request):
    usuario = pedido_controller.pegar_usuario_logado(request)

    if not usuario:
        return RedirectResponse(url="/login", status_code=303)
    
    pedidos = pedido_controller.listar_pedidos_controller(request)

    return templates.TemplateResponse("pgcliente.html", {
        "request": request,
        "usuario": usuario,
        "pedidos": pedidos['pedidos'],
        "nome_usuario": usuario.nome,
    })


@router.post("/criar-pedido")
def criar_pedido(
    request: Request,
    sabores: List[str] = Form(...),
    tamanhos: List[str] = Form(...),
    quantidades: List[int] = Form(...),
    precos: List[float] = Form(...),
    data_entrega: str = Form(...)
):
    usuario = pegar_usuario_logado(request)

    if not usuario:
        return RedirectResponse(url="/login", status_code=303)
    
    itens = []
    for sabor, tamanho, quantidade, preco in zip(sabores, tamanhos, quantidades, precos):
        itens.append({
            "sabor": sabor,
            "tamanho": tamanho,
            "quantidade": quantidade,
            "preco_unitario": preco
        })

    return pedido_controller.criar_pedido_controller(request, itens, data_entrega)

@router.post("/cancelar-pedido/{id_pedido}")
def cancelar_pedido(id_pedido: int, request: Request):
    usuario = pegar_usuario_logado(request)
    if not usuario: 
        return RedirectResponse(url="/login", status_code=303)
    
    pedido_model.excluir_pedido(id_pedido)
    return RedirectResponse(url="/meus-pedidos", status_code=303)
    

