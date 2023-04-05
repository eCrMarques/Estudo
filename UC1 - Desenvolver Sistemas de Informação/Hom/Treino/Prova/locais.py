class Locais:
    def __init__(self, rotas, npc=None, selvagens=None ,mark=None, centro=None ):
        self.npc=npc
        self.mark=mark
        self.centro=centro
        self.selvagens=selvagens
        self.rotas=rotas
    
    def centro(self):
        pass

    def mark(self):
        pass

Pallet=Locais('Rota1')
Rota1=Locais(['Viridian','Pallet'],selvagens=['Pidgey','Rattata'])

Viridian=Locais(['Rota22','Rota2','Rota1'],npc=['Market','Centro'])
Rota22=Locais(['Liga Pokemon','Viridian'],selvagens=['Rattata','NidoranF','NidoranM','Spearow'])
Rota2=Locais(['ViridianForest','Viridian'],selvagens=['Rattata','Pidgey','Weedle','Caterpie'])
ViridianForest=Locais(['Pewter',"Diglett's Cave",'Rota2'],selvagens=['Weedle','Caterpie','Kakuna','Metapod','Pikachu'])
DiglettCave=Locais(['Pewter','Vermillion','Rota2'],selvagens=['Diglett','Dugtrio'])

Pewter=Locais(['Rota3',"Diglett's Cave",'ViridianForest'],npc=['Centro','Market'])
Rota3=Locais(['Mt.Moon','Viridian'],selvagens=['Pidgey','Spearow','Jigglypuff'])
MtMoon=Locais(['Rota4','Rota3'],selvagens=['Zubat','Geodude','Paras','Clefairy','Sandshrew'])
Rota4=Locais(['Cerulean','Mt.Moon'],selvagens=['Rattata','Spearow','Ekans','Sandshrew','Mankey'])

Cerulean=Locais(['Rota24','Rota5','Rota9','Rota4'],npc=['Market','Centro'])
Rote24=Locais(['Cerulean','Rota25'],selvagens=['Weedle','Oddish','Pidgey','Abra'])
Rota25=Locais("Rota24",selvagens=['Weedle','Caterpie','Bellsprout','Kakuna','Metapod','Pidgey','Abra','Venonat'])
Rota5=Locais(['Passagem Subsolo','Cerulean'],selvagens=['Oddish','Bellsprout','Pidgey','Mankey','Meowth','NidoranF'])
PassagemSubsolo=Locais(['Rota5','Rota6'])
Rota6=Locais(['Vermelion City','Passagem Subsolo'],selvagens=['Pidgey','Oddish','Mankey','Pidgeotto'])

Vermilion=Locais(['Rota11','Navio Anne','Rota6'],npc=['Centro','Market'])
Rota11=Locais(['Vermilion'],selvagens=['Ekans','Sandshrew','Spearow','Drowzee','Raticate','Nidorina'])

Saffron=Locais(['Rota8','Rota7'],npc=['Centro','Market'])
Rota7=Locais(['Saffron'],selvagens=['Pidgey','Pidgeotto','Oddish','Bellsprout','Mankey','Growlithe','Vuplix'])
Rota8=Locais(['LavenderTown','Saffron'],selvagens=['Pidgey','Rattata','Ekans','Vupix','Growlithe','Kadabra','Pidgeotto'])

Celadon=Locais(['Rota16','Rota7'],npc=['Centro','Market'])
Rota16=Locais(['Rota17','Celadon'],selvagens=['Spearow','Rattata','Doduo','Raticate','Fearow'])
Rota17=Locais(['Rtoa18','Rota16'],selvagens=['Spearow','Raticate','Spearow','Fearow','Ponyta'])

Rota18=Locais(['Fuchsia','Rota17'],selvagens=['Spearow','Doduo','Raticate','Fearow'])
Fuchsia=Locais(['Rota15','Rota18'],npc=['Centro','Market'])
Rota15=Locais(['Rota 14','Fuchsia'],selvagens=['Oddish','Bellsprout','Venonat','Ditto','Pidgeotto','Gloom','Weepinbell'])
Rota14=Locais(['Rota13','Rota15'],selvagens=['Bellsprout','Venonat','Ditto','Pidgeotto','Gloom','Weepinbell','Venomoth'])
Rota13=Locais(['Rota11','Rota12','Rota 14'],selvagens=['Gloom','Weepinbell','Pidgeotto','FarfetchD','Ditto'])

Lavender=Locais(['Rota10','LavenderTown'],npc=['Centro','Market'])
LavenderTown=Locais('Lavender',selvagens=['Gastly','Cubone','Haunter'])
Rota10=Locais(['Rock Tunnel','LavenderTown'],selvagens=['Voltorb','Spearow','Ekans','Sandshrew','Mangnemite','NidoranF','NidoranM','Machop','Raticate'])
RockTunnel=Locais(['Rota9','Rota10'],selvagens=['Zubat','Geodude','Machop','Onix'])
Rota9=Locais(['Cerulean','Rock Tunnel'],selvagens=['Rattata','Spearow','Ekans','Sandshrew','Fearow','Nidorino','Nidorina'])

Rota19=Locais(['Sea Island','Fuchsia'],selvagens=['Tentacool','Magikarp','Poliwag','Goldeen','Shellder','Horsea','Staryu','Tentacruel'])
SeaIsland=Locais(['Rota20','Rota19'],selvagens=['Seel','Horsea','Krabby','Shellder','Staryu','Slowpoke','Psyduck','Golduck','Slowbro','Dewgong','Seadra','Kingler','Articuno'])
Rota20=Locais(['Cinnabar','Sea Island'],selvagens=['Tentacool','Magikarp','Tentacruel','Staryu','Shelder'])

Cinnabar=Locais(['Pokemon Mansion','Rota22','Rota20'],npc=['Centro','Market'])
Mansion=Locais(['Cinnabar'],selvagens=['Magmar','Grimmer','Muk','Koffing','Weezing','Vulpix','Ninetales','Rapidash'])
Rota22=Locais(['Pallet','Cinnabar'],selvagens=['Tentacruel','Tangela','Pidgeotto','Raticate','Pidgeot'])


def rotas(nome):
    match nome:
        case 'Rota1':
            return Rota1
        case 'Rota22':
            return Rota22
        case 'Rota2':
            return Rota2
        case 'Rota3':
            return Rota3
        case 'Rote24':
            return Rote24
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
        case 'Rota10':
            return Rota10
        case 'Rota9':
            return Rota9
        case 'Rota19':
            return Rota19
        case 'Rota20':
            return Rota20
        case 'Rota22':
            return Rota22
