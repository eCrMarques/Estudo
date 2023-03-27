# Problema: Crie uma classe "Pessoa" com os atributos "nome" e "idade". Crie um método "apresentar" que imprime na tela uma mensagem com o nome e a idade da pessoa.

# Instruções: Crie um objeto da classe "Pessoa" com nome "Maria" e idade 30. Chame o método "apresentar" do objeto criado.

# Resultado esperado: "Meu nome é Maria e tenho 30 anos."


class Pessoa:
    def __init__(self,nome,idade):
        self.nome =nome
        self.idade= idade

    def apresentar(self):
        print(f'Meu nome é {self.nome}, Tenho {self.idade} anos.')

pessoa1=Pessoa('Maria',30)

pessoa1.apresentar()


# Problema: Crie uma classe "Circulo" com o atributo "raio". Crie um método "calcularArea" que retorna a área do círculo. Considere π = 3.14.

# Instruções: Crie um objeto da classe "Circulo" com raio 5. Calcule e imprima a área do círculo usando o método "calcularArea".

# Resultado esperado: 78.5

class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def CalcularArea(self):
        area = (self.raio**2)*3.14
        return f'a area do circulo é {area}'

circulo1=Circulo(4)
print(circulo1.CalcularArea())


# Problema: Crie uma classe "Livro" com os atributos "titulo", "autor" e "ano". Crie um método "informacoes" que retorna uma string com as informações do livro no formato "titulo - autor (ano)".

# Instruções: Crie um objeto da classe "Livro" com título "O Senhor dos Anéis", autor "J. R. R. Tolkien" e ano 1954. Chame o método "informacoes" do objeto criado e imprima o resultado.

# Resultado esperado: O resultado esperado é que o método "informacoes" retorne a string "O Senhor dos Anéis - J. R. R. Tolkien (1954)".


class Livro:
    def __init__(self,titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    def informacoes(self):
        return f'{self.titulo} - {self.autor}  ({self.ano})'
    
livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954)
print(livro1.informacoes())

# Problema: Crie uma classe "Funcionario" com os atributos "nome", "salario" e "departamento". 
# Crie um método "aumentarSalario" que recebe um valor percentual como parâmetro e aumenta o salário do funcionário de acordo com o valor informado.
# Crie também um método "informacoes" que retorna uma string com as informações do funcionário no formato "nome - departamento - salario".

class Funcionario():
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def aumentarSalario(self, salario):
        self.salario = salario / 100 + self.salario
    
    def informacoes(self):
        print(f"{self.nome} - {self.departamento} - {self.salario}")


pessoa = Funcionario("João", 3000, "Vendas")
 
pessoa.informacoes()


#Problema: Crie uma classe "Carro" com os atributos "marca", "modelo" e "ano". Crie um método "informacoes" 
# que retorna uma string com as informações do carro no formato "marca - modelo - ano". 
# Crie também um método "acelerar" que recebe uma velocidade como parâmetro e imprime uma mensagem 
# indicando que o carro acelerou para a velocidade informada.

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def informacoes(self):
        return f"{self.marca} - {self.modelo} - {self.ano}"
    
    def acelerar(self,velocidade):
        print(f'O carro acelerou para {velocidade}Km/h')

carro1=Carro('Fiat','Uno','2000')
print(carro1.informacoes())
carro1.acelerar(80)