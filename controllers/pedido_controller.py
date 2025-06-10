from fastapi import Request
from fastapi.responses import RedirectResponse
from typing import Optional
from datetime import datetime
from models import pedido_model
from models.carrinho_model import Carrinho
from controllers import usuario_controller


def pegar_usuario_logado(request: Request):
    """
    Retorna o objeto usuário logado com base na sessão.
    Se não houver usuário logado, retorna None.
    """
    usuario_sessao = request.session.get("usuario")
    if usuario_sessao:
        email = usuario_sessao.get("email")
        if email:
            return usuario_controller.buscar_por_email(email)
    return None


def calcular_desconto(total: float, cupom: Optional[str]) -> float:
   
    descontos = {
        "PROMO10": 0.10,  
        "PROMO20": 0.20,  
        "FRETEGRATIS": 0.15,
    }

    if cupom and cupom.upper() in descontos:
        desconto_percentual = descontos[cupom.upper()]
        desconto_valor = total * desconto_percentual
        total_com_desconto = total - desconto_valor
        return round(total_com_desconto, 2)
    return total


def criar_pedido_controller(request: Request, itens: list, data_entrega: str, cupom: Optional[str] = None):
    usuario = pegar_usuario_logado(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=303)

    id_usuario = usuario.id
    total = sum(item['preco_unitario'] * item['quantidade'] for item in itens)

    desconto_percentual = {
        "PIZZA10": 0.10,
        "PIZZA20": 0.20,
        "FRETEGRATIS": 0.15
    }.get(cupom.upper(), 0.0) if cupom else 0.0

    desconto_valor = round(total * desconto_percentual, 2)
    valor_final = total - desconto_valor

    id_pedido = pedido_model.criar_pedido(
        id_usuario=id_usuario,
        total=total,
        data_entrega=data_entrega,
        cupom=cupom,
        desconto=desconto_valor,
        valor_final=valor_final
    )

   
    for item in itens:
        pedido_model.adicionar_item_pedido(
            id_pedido=id_pedido,
            sabor=item['sabor'],
            tamanho=item['tamanho'],
            quantidade=item['quantidade'],
            preco_unitario=item['preco_unitario']
        )

    Carrinho.limpar_carrinho(request.session)
    return RedirectResponse(url='/meus-pedidos', status_code=303)


def listar_pedidos_controller(request: Request):
    """
    Lista todos os pedidos do usuário logado.
    """
    usuario = pegar_usuario_logado(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=303)

    id_usuario = usuario.id
    pedidos = pedido_model.listar_pedidos_por_usuario(id_usuario)

    for pedido in pedidos:
        itens = pedido_model.listar_itens_do_pedido(pedido['id_pedido'])
        pedido['itens'] = itens

    return {"pedidos": pedidos}


def alterar_status_pedido_controller(id_pedido: int, novo_status: str):
    """
    Altera o status de um pedido (usado na parte administrativa).
    """
    pedido_model.alterar_status_pedido(id_pedido, novo_status)
    return {"mensagem": f"Status do pedido {id_pedido} alterado para {novo_status}"}
