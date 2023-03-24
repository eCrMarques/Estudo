class Conta:
    def __init__(self, nconta, saldo):
        self._saldo = saldo
        self._nConta =nconta
    
    def getsaldo(self):
        return f'Saldo: {self._saldo}\n'
    
    def setsaldo(self, novosaldo):
        if self._validar(novosaldo):
            print(f'Saldo alterado para {novosaldo}')
            self._saldo= novosaldo
        else:
            print(f'Alteração para {novosaldo} Invalida')

    def sacar(self, valor):
        if self._validar(valor) and self._saldo>valor:
            print(f'{valor} Sacado com sucesso')
            self._saldo=self._saldo-valor
        else:
            print(f'Valor de {valor} Indisponivel')
    
    def _validar(self,saldo):
        if saldo>=0:
            return True
        else:
            return False

conta1 =Conta('J',1546)    
print(conta1.getsaldo())
conta1.sacar(300)
print(conta1.getsaldo())


conta1.setsaldo(321)
print(conta1.getsaldo())

conta1.setsaldo(-200)
print(conta1.getsaldo())
conta1.sacar(400)
print(conta1.getsaldo())