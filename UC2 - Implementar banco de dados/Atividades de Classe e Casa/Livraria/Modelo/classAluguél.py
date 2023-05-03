class Aluguel:
    def __init__(self, id, _idCliente, idLivro, Entregue):
        self._idAluguel =id
        self._idCliente =_idCliente
        self._idLivro = idLivro
        self._Entregue = Entregue

    def inserirAluguel(self):
        sql=f"""
        INSERT INTO "Aluguel"
        Values(default,'{self._idCliente}','{self._idLivro}',default)
        """

        return sql
    
    def Retirar(self):
        sql=f""""
        UPDATE "Livro" 
        set
        "Quantidade" = "Quantidade" - '1'
        where
        "id_Cliente"='{self._idLivro}' """

        return sql