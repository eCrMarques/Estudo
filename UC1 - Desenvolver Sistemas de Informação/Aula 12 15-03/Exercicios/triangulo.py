# 1. Classe Triangulo: Crie uma classe que modele um triangulo:
# – Atributos: LadoA, LadoB, LadoC
# – Métodos: calcular Perímetro, getMaiorLado;
# Crie um programa que uFlize esta classe. Ele deve pedir ao usuário que informe as
# medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir
# sua área e maior lado.

class Triangulo:
    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA =LadoA
        self.LadoB =LadoB
        self.LadoC =LadoC

    def Perimetro(self):
        perimetro= self.LadoA+self.LadoB+self.LadoC
        print(perimetro)
    
    def MaiorLado(self):
        Lista=[self.LadoA,self.LadoB,self.LadoC]
        maior=Lista[0]
        for item in Lista:
            if item>maior:
                item=item
                maior=item
        print(f'O Lado maior é {maior} do {Lista[str(item)]}')

trio =Triangulo(1,4,5)
trio.MaiorLado()
trio.Perimetro()