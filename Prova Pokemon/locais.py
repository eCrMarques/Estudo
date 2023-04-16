class Locais:
    def __init__(self, rotas, npc=None, selvagens=None ,mark=None, centro=None ):
        self.npc=npc
        self.mark=mark
        self.centro=centro
        self.selvagens=selvagens
        self.rotas=rotas

ginasio={'Pallet':['Pedra','Brock',['Geodude','Onix']],
        'Cerulean':['Agua','Misty',['Staryu','Starmie',]],
         'Vermilion':['Eletrico','Lt.Surge',['Voltorb','Pikachu','Raichu']],
          'Celadon':['Grama','Erika',['Victreebel','Tangela','Vileplume']], 
          'Fuchsia':['Veneno','Koga',['Koffing','Koffing','Muk','Weezing']],
          'Saffron':['Psiquico','Sabrina',['Kadabra','Mr. Mime','Venomoth','Alakazam']],
          'Cinnabar':['Fogo','Blaine',['Growlithe','Ponyta','Rapidash','Arcanine']],
          'Viridian':['Terra','Giovanni',['Rhyhorn','Dugtrio','Nidoqueen','Nidoking','Rhyhorn']]
          }

Pallet=Locais('Rota1')
Rota1=Locais(['Viridian','Pallet'],selvagens=['Pidgey','Rattata'])

Viridian=Locais(['Rota2','Rota22','Rota1'],npc=['Market','Centro'])
Rota22=Locais(['LigaPokemon','Viridian'],selvagens=['Rattata','NidoranF','NidoranM','Spearow'])
Rota2=Locais(['ViridianForest','Viridian'],selvagens=['Rattata','Pidgey','Weedle','Caterpie'])
ViridianForest=Locais(['Pewter','Rota2'],selvagens=['Weedle','Caterpie','Kakuna','Metapod','Butterfree','Pikachu'])
DiglettCave=Locais(['Pewter','Vermillion','Rota2'],selvagens=['Diglett','Dugtrio'])

Pewter=Locais(['Rota3',"DiglettCave",'ViridianForest'],npc=['Centro','Market'])
Rota3=Locais(['MtMoon','Pewter'],selvagens=['Pidgey','Spearow','Jigglypuff','Wigglytuff'])
MtMoon=Locais(['Rota4','Rota3'],selvagens=['Zubat','Geodude','Paras','Clefairy','Sandshrew'])
Rota4=Locais(['Cerulean','MtMoon'],selvagens=['Rattata','Spearow','Ekans','Sandshrew','Mankey'])

Cerulean=Locais(['Rota24','Rota5','Rota9','Rota4'],npc=['Market','Centro'])
Rota24=Locais(['Cerulean','Rota25'],selvagens=['Weedle','Oddish','Pidgey','Abra'])
Rota25=Locais("Rota24",selvagens=['Weedle','Caterpie','Bellsprout','Kakuna','Metapod','Pidgey','Abra','Venonat'])
Rota5=Locais(['PassagemSubsolo','Cerulean'],selvagens=['Oddish','Bellsprout','Pidgey','Mankey','Meowth','NidoranF'])
PassagemSubsolo=Locais(['Rota5','Rota6'])
Rota6=Locais(['Vermilion','Saffron','PassagemSubsolo'],selvagens=['Pidgey','Oddish','Mankey','Primeape','Pidgeotto'])

Vermilion=Locais(['Rota11','Navio Anne','Rota6'],npc=['Centro','Market'])
Rota11=Locais(['Rota13','Vermilion'],selvagens=['Ekans','Sandshrew','Spearow','Drowzee','Raticate','Nidorina'])

Saffron=Locais(['Rota8','Rota7'],npc=['Centro','Market'])
Rota7=Locais(['Saffron'],selvagens=['Pidgey','Pidgeotto','Oddish','Bellsprout','Mankey','Growlithe','Vulpix'])
Rota8=Locais(['LavenderTown','Saffron'],selvagens=['Pidgey','Rattata','Ekans','Vulpix','Growlithe','Kadabra','Alakazam','Hypno','Pidgeotto'])

Celadon=Locais(['Rota16','Rota7'],npc=['Centro','Market'])
Rota16=Locais(['Rota17','Celadon'],selvagens=['Spearow','Rattata','Doduo','Raticate','Fearow'])
Rota17=Locais(['Rota18','Rota16'],selvagens=['Spearow','Raticate','Spearow','Fearow','Ponyta'])

Rota18=Locais(['Fuchsia','Rota17'],selvagens=['Spearow','Doduo','Raticate','Fearow'])
Fuchsia=Locais(['Rota19','Saffari','Rota15','Rota18'],npc=['Centro','Market'])
Rota15=Locais(['Rota 14','Fuchsia'],selvagens=['Oddish','Bellsprout','Venonat','Ditto','Pidgeotto','Gloom','Weepinbell'])
Rota14=Locais(['Rota13','Rota15'],selvagens=['Bellsprout','Venonat','Ditto','Pidgeotto','Gloom','Weepinbell','Venomoth'])
Rota13=Locais(['Rota14','Rota12','Rota11'],selvagens=['Gloom','Weepinbell','Pidgeotto','FarfetchD','Ditto'])

Lavender=Locais(['Rota8','Rota10','Rota12','LavenderTown'],npc=['Centro','Market'])
LavenderTown=Locais(['Lavender'],selvagens=['Gastly','Cubone','Haunter','Gengar'])
Rota10=Locais(['RockTunnel','LavenderTown'],selvagens=['Voltorb','Spearow','Ekans','Sandshrew','Mangnemite','NidoranF','NidoranM','Machop','Raticate'],npc=['Centro'])
RockTunnel=Locais(['Rota9','Rota10'],selvagens=['Zubat','Golbat','Graveler','Machoke','Onix','Hitmonlee','Hitmonchan','Machamp'])
Rota9=Locais(['Cerulean','RockTunnel'],selvagens=['Rattata','Spearow','Ekans','Arbok','Sandshrew','Fearow','Nidorino','Nidorina'])

Rota19=Locais(['SeaIsland','Fuchsia'],selvagens=['Tentacool','Magikarp','Poliwag','Goldeen','Shellder','Horsea','Staryu','Tentacruel','Vaporeon','Gyarados'])
SeaIsland=Locais(['Rota20','Rota19'],selvagens=['Jynx','Seel','Horsea','Krabby','Shellder','Staryu','Slowpoke','Psyduck','Golduck','Slowbro','Dewgong','Seadra','Kingler','Articuno'])
Rota20=Locais(['Cinnabar','SeaIsland'],selvagens=['Tentacool','Magikarp','Tentacruel','Staryu','Shelder','Poliwrath'])

Cinnabar=Locais(['Mansion','Rota21','Rota20'],npc=['Centro','Market'])
Mansion=Locais(['Cinnabar'],selvagens=['Magmar','Grimer','Muk','Koffing','Weezing','Vulpix','Ninetales','Rapidash','Flareon'])
Rota21=Locais(['Pallet','Cinnabar'],selvagens=['Tentacruel','Tangela','Pidgeotto','Raticate','Pidgeot'])

PowerPlant=Locais(['RockTunnel'],selvagens=['Pikachu','Electabuzz','Magneton','Electrode','Zapdos','Raichu','Joleton'])
Rota12=Locais(['Lavender','Rota11'],selvagens=['Weepinbell','Pidgeotto','FarfetchD','Slowbro','Snorlax','Seadra'])
Saffari=Locais(['Fuchsia'],selvagens=['Nidoking','Vileplume','Nidoqueen','Exeggutor','Licktung','Vileplume','Kangaskhan','Evee','Pinsir','Chansey','Exeggcute','Mr. Mime'])

LigaPokemon=Locais(['Rota23','Rota22'],npc=['Centro','Market'])
Rota23=Locais(['VictoryRoad',],selvagens=['Ditto','Fearow','Arbok','Sandslash','Kingler','Poliwhirl','Primeape'])
VictoryRoad=Locais(['Rota23','LigaPokemon'],selvagens=['Onix','Machoke','Machamp','Venomoth','Moltres','Mew','Mewtwo','Golbat','Marowak','Golem'])
def rotas(nome):
    match nome:
        case 'VictoryRoad':
            return VictoryRoad
        case 'PowerPlant':
            return PowerPlant
        case 'Saffari':
            return Saffari
        case 'Rota21':
            return Rota21
        case 'Rota4':
            return Rota4
        case 'ViridianForest':
            return ViridianForest
        case 'Rota1':
            return Rota1
        case 'Rota2':
            return Rota2
        case 'Rota3':
            return Rota3
        case 'Rota24':
            return Rota24
        case 'Rota25':
            return Rota25
        case 'Rota5':
            return Rota5
        case 'Rota6':
            return Rota6
        case 'Rota11':
            return Rota11
        case 'Rota7':
            return Rota7
        case 'Rota8':
            return Rota8
        case 'Rota16':
            return Rota16
        case 'Rota17':
            return Rota17
        case 'Rota18':
            return Rota18
        case 'Rota15':
            return Rota15
        case 'Rota14':
            return Rota14
        case 'Rota13':
            return Rota13
        case 'Rota12':
            return Rota12
        case 'Rota10':
            return Rota10
        case 'Rota9':
            return Rota9
        case 'Rota19':
            return Rota19
        case 'Rota23':
            return Rota23
        case 'Rota20':
            return Rota20
        case 'Rota22':
            return Rota22
        case 'DiglettCave':
            return DiglettCave
        case 'MtMoon':
            return MtMoon
        case 'LavenderTown':
            return LavenderTown
        case 'RockTunnel':
            return RockTunnel
        case 'SeaIsland':
            return SeaIsland
        case 'Mansion':
            return 