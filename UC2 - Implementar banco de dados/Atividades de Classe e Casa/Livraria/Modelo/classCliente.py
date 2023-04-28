class Cliente:
    def __init__(self, Id, Nome, Telefone, Cpf):
        self._id=Id
        self._nome=Nome
        self._Telefone=Telefone
        self._Cpf=Cpf
    
    def inserirCliente(self):
        sql=f"""
        INSERT INTO "Cliente"
        Values(default,'{self._nome}','{self._Telefone}','{self._Cpf}')
        """
        
        return sql