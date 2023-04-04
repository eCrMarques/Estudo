from Textos import *
from Treinadores import *
from locais import *

Vezes=0

cidadeAnterior=''
cidade='Pallet'
cidades=['LigaPokemon','PassagemSubsolo','Pallet','Viridian','Pewter','Cerulean','Vermilion','Saffron','Celadon','Fuchsia','Lavender','Cinnabar']


def CurarPokemon(pokemons):
    if type(pokemons)== list:
        for pokemon in pokemons:
            pokemon.hp=pokemon.hpa()
    else:
        pokemons.hp=pokemon.hpa()



def opc(escolha,op1,op2,op3,op4,op5):
    match escolha:
        case '1':
            return op1
        case '2':
            return op2
        case '3':
            return op3
        case '4':
            return op4
        case '5':
            return op5
        case _:
            pass
    opçõesCidade(cidadeAnterior)

def Aventura(local):
    global cidade
    global cidadeAnterior
    lista=listaLocais(local.rotas)
    num=input()

    Nome=opc(num,lista[0],lista[1],lista[2],lista[3],lista[4])
    if Nome=='' or num.isnumeric==False:
        opçõesCidade(cidadeAnterior)
    if Nome not in cidades:
        Ganhador=True
        for pokemon in Player.pokemons:
            if pokemon.hp>0:
                Ganhador=False
        if Ganhador:
            print('Seus Pokemons estão machucados vá ao Centro Pokemon')
            opçõesCidade(cidadeAnterior)
        else:
            rota=rotas(Nome)
            resultado=False
            for i in range(random.randrange(1,4)):
                selvagem=NomePokemon(rota.selvagens)
                resultado=Player.batalha(selvagem)
            if resultado:
                cidade=Nome
                print(resultado)
                opçõesCidade(Nome)
            else:
                print(resultado)
                opçõesCidade(cidade)
    else:
        cidade=Nome
        opçõesCidade(Nome)

def lutasTreinadores(local):
    Nome=random.choice(['Josh','Blue','Red','Samanta','Jay','Peter','Kel','Trace','Ry','Fyer','Aly','Zye'])
    listaPokemons=[]
    if local not in cidades:
        rota=rotas(local)  
        for i in range(random.randrange(1,4)):
            listaPokemons.append(NomePokemon(rota.selvagens))
        Rival=Oponente(Nome,listaPokemons,random.randrange(300,750))
        Player.batalha(Rival)
        Ganhador=False
        for pokemon in Player.pokemons:
            if pokemon.hp>0:
                Ganhador=True
        if Ganhador:
            opçõesCidade(cidade)
        else:
            opçõesCidade(cidadeAnterior)

    else:
        print('Não há Treinadores Por Aqui')
        opçõesCidade()
 
def Explorar(cidade):
    print(f'''\t\t---Local atual: {cidade}   --- ''')
    if cidade in cidades:
        global cidadeAnterior
        match cidade:
            case "LigaPokemon":
                cidadeAnterior="LigaPokemon"
                Aventura(LigaPokemon)
            case "Pallet":
                cidadeAnterior="Pallet"
                Aventura(Pallet)
                
            case 'Viridian':
                cidadeAnterior="Viridian"
                Aventura(Viridian)

            case 'Pewter':
                cidadeAnterior="Pewter"
                Aventura(Pewter)
            
            case 'Cerulean':
                cidadeAnterior="Cerulean"
                Aventura(Cerulean)

            case 'Vermilion':
                cidadeAnterior="Vermilion"
                Aventura(Vermilion)
            
            case 'Saffron':
                cidadeAnterior="Saffron"
                Aventura(Saffron)

            case 'Celadon':
                cidadeAnterior="Celadon"
                Aventura(Celadon)

            case 'Fuchsia':
                cidadeAnterior="Fuchsia"
                Aventura(Fuchsia)
            
            case 'Cinnabar':
                cidadeAnterior="Cinnabar"
                Aventura(Cinnabar)
            
            case 'Lavender':
                cidadeAnterior="Lavender"
                Aventura(Lavender)
            case 'PassagemSubsolo':
                Aventura(PassagemSubsolo)
    else:
        rota=rotas(cidade)
        Aventura(rota)

def opçõesCidade(Nome=None):
    if Nome==None:
        Nome=cidade
    else:
        Nome=Nome
    print(f'''
        \t---Local atual: {Nome}--- \n
        1-- Explorar
        2-- Procurar Treinadores
        3-- Centro Pokemon
        4-- Market
        5-- Perfil''')
    match input(''):
        case '1':
            Explorar(Nome)
        case '2':
            Ganhador=True
            for pokemon in Player.pokemons:
                if pokemon.hp>0:
                    Ganhador=False
            if Ganhador:
                print('Seus Pokemons estão machucados vá ao Centro Pokemon')
                opçõesCidade()
            else:
                lutasTreinadores(Nome)
        case '3':
            if Nome in cidades:
                resposta=Textos('Centro')
                if resposta=='Sim':
                    CurarPokemon(Player.pokemons)
                    print(f'Seu Pokemon Foi curado ')
                    opçõesCidade(Nome)
                else:
                    pass
            else:
                print('Não há Centro Pokemon Por Aqui')
                pass
            opçõesCidade(Nome)
        case '4':
            if Nome in cidades:
                resposta=Textos('Mark')
                if resposta=='Sim':
                    while True:
                        print(f'Dinheiro\t-{Player.dinheiro}-\n')
                        print('1-Poke ball(1x) Preço 200\n2-Great Ball(2x) Preço 500\n3-Ultra Ball(4x) Preço 1200')
                        match input():
                            case '1':
                                if Player.dinheiro>=200:
                                    Player.Mochila('Poke Ball')
                                    print("Compra de PokeBall Com Sucesso")
                                    Player.dinheiro-=200
                                else:
                                    print('Você não tem dinheiro suficiente')
                            case '2':
                                if Player.dinheiro>=500:
                                    Player.Mochila('Great Ball')
                                    print("Compra de Great Ball Com Sucesso")
                                    Player.dinheiro-=500
                                else:
                                    print('Você não tem dinheiro suficiente')
                            case '3':
                                if Player.dinheiro>=1200:
                                    Player.Mochila('Ultra Ball')
                                    print(f"Compra de Ultra Ball Com Sucesso")
                                    Player.dinheiro-=1200
                                else:
                                    print(f'{Player.dinheiro} - Você não tem dinheiro suficiente')
                            case '0':
                                break
                            case _:
                                print('Opçao Inexistente')
                    opçõesCidade(Nome)
                else:
                    print('Volte quando desejar comprar')
                    opçõesCidade(Nome)
            else:
                print('Não há Market Pokemon Por Aqui')
                opçõesCidade(Nome)

            
        case '5':
            print(f'''-----{Player.nome}-----
            1 =-= Mochila
            2 =-= Mapa
            3 =-= Menu''')
            op =input()
            match op:
                case '1':
                    Player.VerMochila()
                    opçõesCidade()
                case '2':
                    print('''Mapa''')
                case '3':
                    Menu(0.05)
                case _:
                    print('Valor Invalido')
                    opçõesCidade(Nome)
        case _:
            print('Valor Invalido')
            opçõesCidade(Nome)



if Vezes==0:
    if Menu(0.005):
        print('''
        Seja Bem-Vindo a sua aventura pokemon, primeiro precisamos saber o seu Nome''')
        Nome=input('')
        Player=Jogador(Nome,dinheiro=3000)
        while True:
            print(f'''\nBom {Nome} Para Começar Sua Aventura Escolha o seu primeiro Pokemon
            1-- Charmander
            2-- Squirtle
            3-- Bulbasaur\n''')
            op =input('')
            match op:
                case '1':
                    Player.capturar('Charizard')
                    break
                case '2':
                    Player.capturar('Squirtle')
                    break
                case '3':
                    Player.capturar('Bulbasaur')
                    break
                case _:
                    print('Opção Inexistente')
            Vezes=1
        opçõesCidade()
                
                
if Vezes>0:
    opçõesCidade()
    
        
    
