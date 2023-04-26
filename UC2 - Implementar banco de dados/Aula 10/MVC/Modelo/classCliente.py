class Cliente:
    def __init__(self, id, nome):
        self.id=id
        self.nome=nome

    def inserirCliente(self):
        sql=f"""INSERT INTO "Cliente"
        Values(default,'{self.nome}')"""

        return sql