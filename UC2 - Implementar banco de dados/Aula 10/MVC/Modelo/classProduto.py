class Produto:
    def __init__(self, id, nome, preço, estoque):
        self.id=id
        self.nome=nome
        self.preço=preço
        self.estoque=estoque

    def inserirProduto(self):
        sql=f"""INSERT INTO "Produto"
        Values(default,'{self.nome}','{self.preço}','{self.estoque}')"""

        return sql