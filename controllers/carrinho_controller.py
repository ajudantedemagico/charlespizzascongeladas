from fastapi import Request
from fastapi.responses import RedirectResponse
from models.carrinho_model import Carrinho
from controllers.usuario_controller import buscar_por_email


def pegar_usuario_logado(request: Request):
    usuario_sessao = request.session.get("usuario")
    if usuario_sessao:
        email = usuario_sessao.get("email")
        if email:
            return buscar_por_email(email)
    return None


def adicionar_itens_carrinho(request: Request, itens: list):
    usuario = pegar_usuario_logado(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=303)

    for item in itens:
        sabor = item.get("sabor")
        tamanho = item.get("tamanho")
        quantidade = item.get("quantidade")
        preco_unitario = item.get("preco_unitario")

        if not all([sabor, tamanho, quantidade, preco_unitario]):
            continue  # Ignora itens incompletos

        try:
            quantidade = int(quantidade)
            preco_unitario = float(preco_unitario)
        except (ValueError, TypeError):
            continue  # Ignora itens com dados inválidos

        if quantidade > 0:
            Carrinho.adicionar_item(request.session, sabor, tamanho, quantidade, preco_unitario)

    return RedirectResponse(url="/carrinho", status_code=303)


def remover_item_carrinho(request: Request, sabor: str, tamanho: str):
    usuario = pegar_usuario_logado(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=303)

    Carrinho.remover_item(request.session, sabor, tamanho)
    return RedirectResponse(url="/carrinho", status_code=303)


def limpar_carrinho(request: Request):
    usuario = pegar_usuario_logado(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=303)

    Carrinho.limpar_carrinho(request.session)
    return RedirectResponse(url="/carrinho", status_code=303)


def listar_itens_carrinho(request: Request):
    usuario = pegar_usuario_logado(request)
    if not usuario:
        return RedirectResponse(url="/login", status_code=303)

    itens_obj = Carrinho.obter_carrinho(request.session)
    total = Carrinho.calcular_total(request.session)

    # Transforma os objetos em dicionários e adiciona subtotal para cada item
    itens = []
    for item in itens_obj:
        item_dict = item.to_dict()
        # Calcula subtotal = quantidade * preco_unitario
        item_dict['subtotal'] = item_dict.get('quantidade', 0) * item_dict.get('preco_unitario', 0.0)
        itens.append(item_dict)

    endereco = f"{usuario.rua}, {usuario.numero}" if usuario.rua and usuario.numero else "Endereço não cadastrado"

    return {
        "nome_usuario": usuario.nome,
        "endereco": endereco,
        "itens_carrinho": itens,
        "total_carrinho": total
    }
