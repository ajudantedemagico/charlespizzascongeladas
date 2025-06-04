from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List
from controllers import carrinho_controller

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/carrinho", response_class=HTMLResponse)
async def mostrar_carrinho(request: Request):
    dados_carrinho = carrinho_controller.listar_itens_carrinho(request)
    if isinstance(dados_carrinho, RedirectResponse):
        return dados_carrinho
    return templates.TemplateResponse("carrinho.html", {"request": request, **dados_carrinho})


@router.post("/carrinho/adicionar")
async def adicionar_itens(
    request: Request,
    sabores: List[str] = Form(...),
    tamanhos: List[str] = Form(...),
    quantidades: List[int] = Form(...),
    precos_unitarios: List[float] = Form(...)
):
    itens = []
    for sabor, tamanho, quantidade, preco in zip(sabores, tamanhos, quantidades, precos_unitarios):
        if quantidade > 0:
            itens.append({
                "sabor": sabor,
                "tamanho": tamanho,
                "quantidade": quantidade,
                "preco_unitario": preco
            })
    return carrinho_controller.adicionar_itens_carrinho(request, itens)


@router.post("/carrinho/remover")
async def remover_item(request: Request, sabor: str = Form(...), tamanho: str = Form(...)):
    return carrinho_controller.remover_item_carrinho(request, sabor, tamanho)


@router.post("/carrinho/limpar")
async def limpar(request: Request):
    return carrinho_controller.limpar_carrinho(request)
