class Compra:
    def __init__(self, id, idCliente, idProduto, quantidade, valorTotal, Timestamp):
        self.id = id
        self.idCliente = idCliente
        self.idProduto = idProduto
        self.quantidade = quantidade
        self.valorTotal = valorTotal
        self.Timestamp = Timestamp
    
    def InsirarCompra(self,Total):
        sql=f"""
        INSERT INTO "Compra"
        Values(default,'{self.idCliente}','{self.idProduto}','{self.quantidade}','{Total}',default)
        """

        return sql