Pokedex=['Bulbasaur',{'tipo':['GRASS','POISON'],'Hp':45,'Atk':45,'Def':49,'Speed':45},
         'Ivysaur',{'tipo':['GRASS','POISON'],'Hp':60,'Atk':62,'Def':63,'Speed':60},
'Venusaur',{'tipo':['GRASS','POISON'],'Hp':80,'Atk':82,'Def':83,'Speed':80},
'Charmander',{'tipo':{'FIRE'},'Hp':39,'Atk':52,'Def':43,'Speed':65},
'Charmeleon',{'tipo':{'FIRE'},'Hp':58,'Atk':64,'Def':58,'Speed':80},
'Charizard',{'tipo':{'FIRE','FLYING'},'Hp':78,'Atk':84,'Def':78,'Speed':100},
'Squirtle',{'tipo':{'WATER'},'Hp':44,'Atk':48,'Def':65,'Speed':43},
'Wartortle',{'tipo':{'WATER'},'Hp':59,'Atk':63,'Def':80,'Speed':58},
'Blastoise',{'tipo':{'WATER'},'Hp':79,'Atk':83,'Def':100,'Speed':78},
'Caterpie',{'tipo':{'BUG'},'Hp':45,'Atk':30,'Def':35,'Speed':45},
'Metapod',{'tipo':{'BUG'},'Hp':50,'Atk':20,'Def':55,'Speed':30},
'Butterfree',{'tipo':{'BUG','FLYING'},'Hp':60,'Atk':45,'Def':50,'Speed':70},
'Weedle',{'tipo':{'BUG','POISON'},'Hp':40,'Atk':35,'Def':30,'Speed':50},
'Kakuna',{'tipo':{'BUG','POISON'},'Hp':45,'Atk':25,'Def':50,'Speed':35},
'Beedrill',{'tipo':{'BUG','POISON'},'Hp':65,'Atk':90,'Def':40,'Speed':75},
'Pidgey',{'tipo':{'NORMAL','FLYING'},'Hp':40,'Atk':45,'Def':40,'Speed':56},
'Pidgeotto',{'tipo':{'NORMAL','FLYING'},'Hp':60,'Atk':60,'Def':55,'Speed':71},
'Pidgeot',{'tipo':{'NORMAL','FLYING'},'Hp':83,'Atk':80,'Def':75,'Speed':101},
'Rattata',{'tipo':{'NORMAL'},'Hp':30,'Atk':56,'Def':35,'Speed':72},
'Raticate',{'tipo':{'NORMAL'},'Hp':55,'Atk':81,'Def':60,'Speed':97},
'Spearow',{'tipo':{'NORMAL','FLYING'},'Hp':40,'Atk':60,'Def':30,'Speed':70},
'Fearow',{'tipo':{'NORMAL','FLYING'},'Hp':65,'Atk':90,'Def':65,'Speed':100},
'Ekans',{'tipo':{'POISON'},'Hp':35,'Atk':60,'Def':44,'Speed':55},
'Arbok',{'tipo':{'POISON'},'Hp':60,'Atk':95,'Def':69,'Speed':80},
'Pikachu',{'tipo':{'ELECTRIC'},'Hp':35,'Atk':55,'Def':40,'Speed':90},
'Raichu',{'tipo':{'ELECTRIC'},'Hp':60,'Atk':90,'Def':55,'Speed':110},
'Sandshrew',{'tipo':{'GROUND'},'Hp':50,'Atk':75,'Def':85,'Speed':40},
'Sandslash',{'tipo':{'GROUND'},'Hp':75,'Atk':100,'Def':110,'Speed':65},
'NidoranF',{'tipo':{'POISON'},'Hp':55,'Atk':47,'Def':52,'Speed':40},
'Nidorina',{'tipo':{'POISON'},'Hp':70,'Atk':62,'Def':67,'Speed':56},
'Nidoqueen',{'tipo':{'POISON','GROUND'},'Hp':90,'Atk':91,'Def':87,'Speed':76},
'NidoranM',{'tipo':{'POISON'},'Hp':46,'Atk':57,'Def':40,'Speed':50},
'Nidorino',{'tipo':{'POISON'},'Hp':61,'Atk':72,'Def':57,'Speed':65},
'Nidoking',{'tipo':{'POISON','GROUND'},'Hp':81,'Atk':102,'Def':77,'Speed':85},
'Vulpix',{'tipo':{'FIRE'},'Hp':38,'Atk':41,'Def':40,'Speed':65},
'Ninetales',{'tipo':{'FIRE'},'Hp':73,'Atk':76,'Def':75,'Speed':100},
'Zubat',{'tipo':{'POISON','FLYING'},'Hp':40,'Atk':45,'Def':35,'Speed':55},
'Golbat',{'tipo':{'POISON','FLYING'},'Hp':75,'Atk':80,'Def':70,'Speed':90},
'Oddish',{'tipo':{'GRASS','POISON'},'Hp':45,'Atk':50,'Def':55,'Speed':30},
'Gloom',{'tipo':{'GRASS','POISON'},'Hp':60,'Atk':65,'Def':70,'Speed':40},
'Vileplume',{'tipo':{'GRASS','POISON'},'Hp':75,'Atk':80,'Def':85,'Speed':50},
'Mankey',{'tipo':{'FIGHTING'},'Hp':40,'Atk':80,'Def':35,'Speed':70},
'Primeape',{'tipo':{'FIGHTING'},'Hp':65,'Atk':105,'Def':60,'Speed':95}
]

def pokemonstipo(tipo):
    lista=[]
    pokemons=[]
    for i in (Pokedex)[1::2]:
        if tipo in i['tipo']:
            lista.append(Pokedex[(Pokedex.index(i))-1])
    
    return lista
