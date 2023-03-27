class Mãe:
    def __init__(self, nome, sobrenome, numero):
        self.nome =nome
        self.numero =numero
        self.sobrenome  =sobrenome

    def status(self,atk,b):
        print(atk,b)

class Filha(Mãe):
    def __init__(self, nome, sobrenome, numero,atk):
        super().__init__(nome, sobrenome, numero)
        self.atk=atk

    def status(self):
        return super().status(self.atk,b=1)


filha1=Filha('nome','sobrenome','abc',123)
print(filha1.__dict__)
filha1.status()