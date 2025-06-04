class ItemCarrinho:
    def __init__(self, sabor: str, tamanho: str, quantidade: int, preco_unitario: float):
        self.sabor = sabor
        self.tamanho = tamanho
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    @property
    def subtotal(self) -> float:
        return self.preco_unitario * self.quantidade

    def atualizar_quantidade(self, quantidade: int):
        self.quantidade += quantidade

    def to_dict(self):
        return {
            "sabor": self.sabor,
            "tamanho": self.tamanho,
            "quantidade": self.quantidade,
            "preco_unitario": self.preco_unitario
        }


class Carrinho:
    SESSION_KEY = "carrinho"

    @staticmethod
    def obter_carrinho(session: dict) -> list[ItemCarrinho]:
        dados = session.get(Carrinho.SESSION_KEY, [])
        itens = []
        for item in dados:
            item_filtrado = {k: item[k] for k in ["sabor", "tamanho", "quantidade", "preco_unitario"] if k in item}
            itens.append(ItemCarrinho(**item_filtrado))
        return itens

    @staticmethod
    def salvar_carrinho(session: dict, itens: list[ItemCarrinho]):
        session[Carrinho.SESSION_KEY] = [item.to_dict() for item in itens]

    @staticmethod
    def adicionar_item(session: dict, sabor: str, tamanho: str, quantidade: int, preco_unitario: float):
        carrinho = Carrinho.obter_carrinho(session)
        for item in carrinho:
            if item.sabor == sabor and item.tamanho == tamanho:
                item.atualizar_quantidade(quantidade)
                Carrinho.salvar_carrinho(session, carrinho)
                return
        novo_item = ItemCarrinho(sabor, tamanho, quantidade, preco_unitario)
        carrinho.append(novo_item)
        Carrinho.salvar_carrinho(session, carrinho)

    @staticmethod
    def remover_item(session: dict, sabor: str, tamanho: str):
        carrinho = Carrinho.obter_carrinho(session)
        carrinho = [item for item in carrinho if not (item.sabor == sabor and item.tamanho == tamanho)]
        Carrinho.salvar_carrinho(session, carrinho)

    @staticmethod
    def limpar_carrinho(session: dict):
        if Carrinho.SESSION_KEY in session:
            del session[Carrinho.SESSION_KEY]

    @staticmethod
    def calcular_total(session: dict) -> float:
        carrinho = Carrinho.obter_carrinho(session)
        return sum(item.subtotal for item in carrinho)
