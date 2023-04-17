from Textos import *
from Treinadores import *
from locais import *
import json
import datetime

Dp=[]

Vezes=0
Treinando=[]
Login=[]
cidadeAnterior=''
cidade='Pallet'
cidades=['LigaPokemon','PassagemSubsolo','Pallet','Viridian','Pewter','Cerulean','Vermilion','Saffron','Celadon','Fuchsia','Lavender','Cinnabar']

def Idle(Estado,treino=None):

    x=datetime.datetime.now()
    tempo=[x.strftime("%x").split('/'),x.strftime("%X").split(':')]    
    global Login
    encerrar=False
    segundos=[]
    if Estado == 'Treino' and Login!='':
        op=input('Você Deseja encerrar o treino?\ns- Sim n- Não\n')
        if op.lower()=='s':
            encerrar=True
        else:
            return
        if encerrar and Estado=='Treino':
            for i,time in enumerate(Login):
                if time==Login[1]:
                    segundos.append((3600*(int(tempo[i][0])-int(time[0]))))
                    segundos.append((((int(tempo[i][1])-int(time[1]))*60)))
                    segundos.append((int(tempo[i][2])-int(time[2])))
                elif time!=Login[1]:
                    segundos.append((2592000*(int(tempo[i][0])-int(time[0]))))
                    segundos.append((((int(tempo[i][1])-int(time[1]))*86400)))
                    segundos.append(((int(tempo[i][2])-int(time[2]))*86400*12))
            stats=int(sum(segundos)/(1800/len(Treinando)))
            print(f'Você Encerrou o treino..\n Status ganho +{stats}')
            for pokemon in Treinando:
                pokemon._hp+=stats
                pokemon._hpanterior+=stats
                pokemon._atk+=stats
                pokemon._df+=stats
                pokemon._spd+=stats
            Login=''
            return 'Encerrado'

def salvar(Dados=None):
    with open ('Save.json','w') as Jogo:
        global Dp
        dicionario={}
        jogador=[]
        meuTime=[]
        bolsa=[]
        Dptime=[]
        x=datetime.datetime.now()
        tempoAtual=[x.strftime("%x").split('/'),x.strftime("%X").split(':')]
        for item in Player.__dict__.keys():
            if item!='pokemons' and item!='bag':
                jogador.append(Player.__dict__[item])
            if item=='bag':
                bolsa=Player.__dict__[item]
        for pokemon in Player.pokemons:
            lista=[]
            lista.append(pokemon.nome)
            lista.append(pokemon._hp)
            lista.append(pokemon._atk)
            lista.append(pokemon._df)
            lista.append(pokemon._spd)
            lista.append(pokemon._hpanterior)
            meuTime.append(lista)
        dicionario['cidade']=cidade
        dicionario['cidadeAnterior']=cidadeAnterior
        dicionario['Jogador']=jogador
        dicionario['Pokemons']=meuTime
        dicionario['Bolsa']=bolsa
        dicionario["Tempo"]=Login
        if Dados!=None:
            dicionario["Tempo"]=tempoAtual
        for pokemon in Dp:
            lista=[]
            lista.append(pokemon.nome)
            lista.append(pokemon._hp)
            lista.append(pokemon._atk)
            lista.append(pokemon._df)
            lista.append(pokemon._spd)
            lista.append(pokemon._hpanterior)
            Dptime.append(lista)
        Treino=[]
        for pokemon in Treinando:
            lista=[]
            lista.append(pokemon.nome)
            lista.append(pokemon._hp)
            lista.append(pokemon._atk)
            lista.append(pokemon._df)
            lista.append(pokemon._spd)
            lista.append(pokemon._hpanterior)
            Treino.append(lista)
        dicionario["Depot"]=Dptime
        dicionario["Treinando"]=Treino
        json.dump(dicionario,Jogo,indent=1)

def Carregar():
    try:
        with open ('Save.json','r') as Jogo:
            Save=json.load(Jogo)
            global cidade
            global cidadeAnterior
            global Dp
            global Login
            global Treinando
            Treino=[]
            cidade=Save['cidade']
            cidadeAnterior=Save['cidade']
            meutime=[]
            DpTime=[]
            for pokemon in Save['Pokemons']:
                meupokemon=NomePokemon(pokemon[0])
                meupokemon._hp=pokemon[1]
                meupokemon._atk=pokemon[2]
                meupokemon._df=pokemon[3]
                meupokemon._spd=pokemon[4]
                meupokemon._hpanterior=pokemon[5]
                meutime.append(meupokemon)
            for pokemon in Save["Depot"]:
                meupokemon=NomePokemon(pokemon[0])
                meupokemon._hp=pokemon[1]
                meupokemon._atk=pokemon[2]
                meupokemon._df=pokemon[3]
                meupokemon._spd=pokemon[4]
                meupokemon._hpanterior=pokemon[5]
                DpTime.append(meupokemon)
            for pokemon in Save["Treinando"]:
                meupokemon=NomePokemon(pokemon[0])
                meupokemon._hp=pokemon[1]
                meupokemon._atk=pokemon[2]
                meupokemon._df=pokemon[3]
                meupokemon._spd=pokemon[4]
                meupokemon._hpanterior=pokemon[5]
                Treino.append(meupokemon)
            Dp=DpTime
            Treinando=Treino
            if Save["Tempo"]!='' and type(Save["Tempo"]!=list):
                Login=Save["Tempo"]
            print(Login)
            Player=Jogador(Save['Jogador'][0],meutime,Save['Jogador'][1])
            Player.bag=Save['Bolsa']
            return Player
    except:
        return 


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
    opçõesCidade(cidade)
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
                print(f'Um {selvagem.nome} Apareceu !!!!')
                input()
                resultado=Player.batalha(selvagem)
                if 'Pokemon' in str(resultado.__class__):
                    Dp.append(resultado) 
                input()
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
        input()
        Ganhador=False
        for pokemon in Player.pokemons:
            if pokemon._hp>0:     # Verificador de hp do time:
                Ganhador=True
        if Ganhador:
            opçõesCidade(cidade)
        else:
            opçõesCidade(cidadeAnterior) # Perder retorna a Ultima Cidade Visitada
 
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
    salvar()
    print(f'{Login}aaa')
    if Nome==None:
        Nome=cidade
    else:
        Nome=Nome
    Ginasio='Ginasio'
    Residencia='Centro Pokemon\n        4-- Market'
    nP='5'
    if cidade not in cidades:
        Ginasio='Procurar Treinadores'
        Residencia='Treinamento'
        nP='4'
    print(f'''
        \t---Local atual: {Nome}--- \n
        1-- Explorar
        2-- {Ginasio}
        3-- {Residencia}
        {nP}-- Perfil''')
    op=input('')
    if nP=='4' and op=='4':
        op='5'
    match op:
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
                if Nome in cidades:
                    op=input(f'Você Deseja Desafiar o Ginasio de {cidade} do Tipo {ginasio[cidade][0]}\n S-Sim ou N-Não\n')
                    match op.lower():
                        case 's':
                            pokemonsLider=[]
                            for pokemon in ginasio[cidade][2]:
                                pokemonsLider.append(NomePokemon(pokemon))

                            lider=Oponente(ginasio[cidade][1],pokemonsLider,random.randrange(2800,3600))
                            loop(f'Lider {ginasio[cidade][1]} o Desafia !!!!',1,0.005,False)
                            input()
                            Player.batalha(lider)
                            opçõesCidade()
                        case 'n':
                            print('Volte quando desejar Desafiar')
                            opçõesCidade()
                        case _:
                            print('Informe uma opção Correta')

                else:
                    lutasTreinadores(Nome)
        case '3':
            if Nome in cidades:
                resposta=Textos('Centro')   # Centro de Cura, retorna o hp ao valor padrão, com a variavel hpa( HpAnterior)
                if resposta=='Sim':
                    CurarPokemon(Player.pokemons)
                    print(f'Seu Pokemon Foi curado ')
                    opçõesCidade(Nome)
                if resposta=='Guardar':
                    global Dp
                    Dp=Depot([Player,Dp])
                    opçõesCidade(Nome)
                else:
                    pass
            else:
                global Treinando
                if len(Treinando)==0 or Login=='':
                    op=input('Você Deseja Treinar os seus Pokemons??')
                    if op.lower()=='s':
                        while True:
                            print(f'\nMeus Pokemons')
                            for i,pokemon in enumerate(Player.pokemons):
                                print(f'{i+1:3}--{pokemon.nome:12}', end='')
                            pokeTreino=input('Coloque os pokemons que deseja Treinar\ns-Sair\n')
                            if pokeTreino.lower()=='s':
                                break
                            if pokeTreino.isnumeric()==False or int(pokeTreino)>len(Player.pokemons) or len(Player.pokemons)==1:
                                print('Pokemon indisponivel')
                            else:
                                Treinando.append(Player.pokemons[int(pokeTreino)-1])   
                                Player.pokemons.pop(int(pokeTreino)-1)
                                salvar('Tempo')
                                Carregar()
                                print('Treinando:')
                                for pokemon in Treinando:
                                    print(f'|{pokemon.nome:<12}',end='')
                elif Login!='':
                    print('Treinando')
                    for pokemon in Treinando:
                        print(f'|{pokemon.nome:^12}|',end='')
                    print(end='\n')
                    if Idle('Treino')=='Encerrado':
                        for pokemon in Treinando:
                            if len(Player.pokemons)<6:
                                Player.pokemons.append(pokemon)
                            else:
                                Dp.append(pokemon)
                        Treinando.clear()
                        input()
                    opçõesCidade()
                    
                pass
            opçõesCidade(Nome)
        case '4':
            if Nome in cidades:
                resposta=Textos('Mark')
                if resposta=='Sim':
                    while True:
                        print(f'Dinheiro\t-{Player.dinheiro}-\n')
                        print('1-Poke ball(1x) Preço 200\n2-Great Ball(2x) Preço 500\n3-Ultra Ball(4x) Preço 1200\n0 =-= Sair')
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
            3 =-= Sair
            ''')
            op =input()
            match op:
                case '1':
                    Player.VerMochila() # Ver Mochila (Pokemons e Items)
                    opçõesCidade()
                case '2':
                    print('''Mapa''')
                    opçõesCidade(Nome)
                case '3':
                    salvar(Login)
                    exit()
                case _:
                    print('Valor Invalido')
                    opçõesCidade(Nome)
        case _:
            print('Valor Invalido')
            opçõesCidade(Nome)


Player=Carregar()
if Player==None:
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
                
                
else:
    opçõesCidade()