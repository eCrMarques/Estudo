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

    def atualizar(self):
        sql=f"""
        Update "Livro"
        set
        ='{self._nome}'
        '={self._quantidade}'
        '={self._lançamento}')
        where "id_Livro" = '{self._id}'
        """
        
        return sql