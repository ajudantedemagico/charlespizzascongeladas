from fastapi import Request
from fastapi.responses import RedirectResponse
from models import pedido_model


def criar_pedido_controller(request: Request, id_usuario: int, itens: list):
    """
    itens = [
        {"sabor": "Calabresa", "tamanho", "broto", "quantidade": 2, "preco_unitario": 30},
        {"sabor": "Mussarela", "tamanho", "Grande", "quantidade": 1, "preco_unitario": 50}
    ]
    
    """

    total = sum(item['preco_unitario'] * item['quantidade'] for item in itens)


    id_pedido = pedido_model.criar_pedido(id, total)

    for item in itens:
        pedido_model.adicionar_item_pedido(
            id_pedido=id_pedido,
            sabor=item['sabor'],
            tamanho=item['tamanho'],
            quantidade=item['quantidade'],
            preço_unitario=item['preco_unitario']
        )
    return RedirectResponse(url='/meus-pedidos', status_code=303)


def listar_pedidos_controller(request: Request, id_usuario: int):
    pedidos = pedido_model.listar_pedidos_por_usuario(id_usuario)

    for pedido in pedidos:
        itens = pedido_model.listar_itens_do_pedido(pedido['id_pedido'])
        pedido['itens'] = itens

    return {"pedidos": pedidos}


def alterar_status_pedido_controller(id_pedido: int, novo_status: str):
    pedido_model.alterar_status_pedido(id_pedido, novo_status)
    return {"mensagem": f"Status do pedido {id_pedido} alterado para {novo_status}"}

