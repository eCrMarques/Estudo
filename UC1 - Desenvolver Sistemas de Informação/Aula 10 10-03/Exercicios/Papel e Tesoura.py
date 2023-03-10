#Elabore o jogo pedra, papel e tesoura.
import random
p=0
while p!=random.choice(['Pedra', 'Papel', 'Tesoura']):
    print("------Pedra, Papel ou Tesoura------\n Escolha entre: \n1-Pedra\n2-Papel\n3-Tesoura")
    x = input('Escolha:')
    p=x
    r=random.choice(['Pedra', 'Papel', 'Tesoura'])
    print(r)
    if x=='1' and r=='Tesoura':
        print('---YOU WIN---')
        break
    elif x=='2' and r=='Pedra':
        print('---YOU WIN---')
        break
    elif x=='3' and r=='Papel':
        print('---YOU WIN---')
        break
    elif x=='1' and r=='Pedra':
        print('---EMPATOUUU---')
    elif x=='2' and r=='Papel':
        print('---EMPATOUUU---')
    elif x=='3' and r=='Tesoura':
        print('---EMPATOUUU---')
    else:
        print("---VOCÊ PERDEU---")


