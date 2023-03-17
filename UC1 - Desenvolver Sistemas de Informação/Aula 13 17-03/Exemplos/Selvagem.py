import random

def Selvagem():
    dex={'Rattata':{
        'tipo':'Normal',
        'ataque':56,
        'vida':30,
        'velocidade':72,
    },'Pidgey':{
        'tipo':'Voador',
        'ataque':45,
        'vida':40,
        'velocidade':56,},
    'Weedle':{
        'tipo':'Inseto',
        'ataque':35,
        'vida':40,
        'velocidade':50,},
    'Caterpie':{
        'tipo':'Inseto',
        'ataque':30,
        'vida':45,
        'velocidade':45,},
    'Metapod':{
        'tipo':'Inseto',
        'ataque':20,
        'vida':50,
        'velocidade':30,},
    'Kakuna':{
        'tipo':'Inseto',
        'ataque':25,
        'vida':45,
        'velocidade':35,}}
    poke=random.choice(['Rattata','Pidgey','Weedle','Caterpie','Metapod','Kakuna'])
    Selvagem = (poke,dex[poke]['tipo'],dex[poke]['ataque'],dex[poke]['vida'],dex[poke]['velocidade'])
    print(Selvagem)
Selvagem()