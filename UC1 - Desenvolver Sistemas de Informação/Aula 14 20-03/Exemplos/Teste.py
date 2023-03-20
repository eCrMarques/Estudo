txt = 'asdas'
print(txt.find('a'))
print(txt.isnumeric())
print(txt.islower())
print(txt.isdigit())

class A:
   a = 1 # atributo publico
   __b = 2 # atributo privado a class A

class B(A):
   __c = 3 # atributo privado a B
   
   def __init__(self):
     print (self.a)
     print (self.__c)

a = A()
print (a.a) # imprime 1

b = B()
print(b.a,123)
print (b._B__c,'asd') # Imprime __c = 3, muito pouco utilizada, mas existe.
print (b.__b) # Erro, pois __b é privado a classe A.
print (b.__c) # Erro, __c é um atributo privado, somente chamado pela classe.

