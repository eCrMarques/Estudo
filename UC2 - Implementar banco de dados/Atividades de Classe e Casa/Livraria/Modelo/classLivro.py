class Livro:
    def __init__(self, id, nome, quantidade, lançamento):
        self._id=id
        self._nome=nome
        self._quantidade= quantidade
        self._lançamento=lançamento

    def inserirLivro(self):
        sql=f"""
        INSERT INTO "Livro"
        Values(default,'{self._nome}','{self._lançamento}','{self._quantidade}')
        """
        
        return sql