from Textos import *
from Treinadores import *
from locais import *

Vezes=0

cidadeAnterior=''
cidade='Pallet'
cidades=['LigaPokemon','PassagemSubsolo','Pallet','Viridian','Pewter','Cerulean','Vermilion','Saffron','Celadon','Fuchsia','Lavender','Cinnabar']

# Curar Pokemon recebendo o objeto Pokemon e adicionando um Hp salvo Anterior para o Hp Atual
def CurarPokemon(pokemons):
    if type(pokemons)== list:
        for pokemon in pokemons:
            pokemon._hp=pokemon.hpa()
    else:
        pokemons.hp=pokemon.hpa()

# Função Match case Que retorna um nome, Usado em conjunto com outro Match para Retornar Objeto ou Variaveis
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
# Opção de Explorar Recebe uma lista de Rotas disponivel de um Objeto Local, Se a variavel Cidade For uma Rota, Cria-se uma Batalha contra Selvagem, Do Contrario Somente Atualiza a rota para uma Nova Cidade
def Aventura(local):
    global cidade
    global cidadeAnterior
    lista=listaLocais(local.rotas)
    num=input()

    Nome=opc(num,lista[0],lista[1],lista[2],lista[3],lista[4]) #Função Match que em conjunto com a lista de locais Retorna o objeto Do Local
    if Nome=='' or num.isnumeric==False:
        opçõesCidade(cidadeAnterior)
    if Nome not in cidades:
        Ganhador=True
        for pokemon in Player.pokemons:  # Verificação de Hp do Time.
            if pokemon._hp>0:
                Ganhador=False
        if Ganhador:
            print('Seus Pokemons estão machucados vá ao Centro Pokemon')
            opçõesCidade(cidadeAnterior)
        else:
            rota=rotas(Nome) #Variavel rota Recebe o Objeto atravez da Função que retorna Objetos
            resultado=False
            for i in range(random.randrange(1,4)):  # Quantidade de Inimigos
                selvagem=NomePokemon(rota.selvagens)
                resultado=Player.batalha(selvagem)
            if resultado:
                cidade=Nome  # Se Ganhar altera a variavel global cidade Para a Rota Atual
                opçõesCidade(Nome)
            else:
                opçõesCidade(cidade) # Se Perder Volta a Cidade Atual 
    else:
        cidade=Nome  # Se a Rota for uma cidade, Atravessa Sem lutas e altera a cidade atual Para a Nova
        opçõesCidade(Nome)

# Luta entre Treinadores, recebe o Local atual, verifica se não é uma cidade e então cria uma batalha
def lutasTreinadores(local):
    Nome=random.choice(['Josh','Blue','Red','Samanta','Jay','Peter','Kel','Trace','Ry','Fyer','Aly','Zye']) 
    listaPokemons=[]
    if local not in cidades:
        rota=rotas(local)  
        for i in range(random.randrange(1,4)):  #Quantidade Time Inimigo
            listaPokemons.append(NomePokemon(rota.selvagens))   #Time inimigo baseado em Pokemons da Rota Atual
        Rival=Oponente(Nome,listaPokemons,random.randrange(300,750))
        Player.batalha(Rival)
        Ganhador=False
        for pokemon in Player.pokemons:
            if pokemon._hp>0:     # Verificador de hp do time:
                Ganhador=True
        if Ganhador:
            opçõesCidade(cidade)
        else:
            opçõesCidade(cidadeAnterior) # Perder retorna a Ultima Cidade Visitada

    else:
        print('Não há Treinadores Por Aqui')  # se a Rota for uma Cidade, Não há Treinadores
        opçõesCidade()
 
def Explorar(cidade): # Verificar as Cidades existentes e modifica a Atual ou Entra em Rotas
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
        
def opçõesCidade(Nome=None): # Opções dos Locais
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
            for pokemon in Player.pokemons:     # Impedir Lutas se O time estiver zerado
                if pokemon._hp>0:
                    Ganhador=False
            if Ganhador:
                print('Seus Pokemons estão machucados vá ao Centro Pokemon')
                opçõesCidade()
            else:
                lutasTreinadores(Nome)
        case '3':
            if Nome in cidades:
                resposta=Textos('Centro')   # Centro de Cura, retorna o hp ao valor padrão, com a variavel hpa( HpAnterior)
                if resposta=='Sim':
                    CurarPokemon(Player.pokemons)
                    print(f'Seu Pokemon Foi curado ')
                    opçõesCidade(Nome)
                else:
                    pass
            else:
                print('Não há Centro Pokemon Por Aqui')  # Se o Local Não se tratar de Cidade
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
                                if Player.dinheiro>=200:        # Adiciona itens a Mochila e retira valor 
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
            ''')
            op =input()
            match op:
                case '1':
                    Player.VerMochila() # Ver Mochila (Pokemons e Items)
                    opçõesCidade()
                case '2':
                    print('''Mapa''')
                case _:
                    print('Valor Invalido')
                    opçõesCidade(Nome)
        case _:
            print('Valor Invalido')
            opçõesCidade(Nome)


# Principal
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
                    Player.capturar('Charmander')
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
