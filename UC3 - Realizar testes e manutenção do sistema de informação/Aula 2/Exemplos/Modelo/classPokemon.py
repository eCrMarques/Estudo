class Pokemon:
    def __init__(self, númeroDex, Espécie, Altura, Peso, Tipo, Região="Kanto"):
        self.númeroDex = númeroDex
        self.Espécie = Espécie
        self.Altura = Altura
        self.Peso = Peso
        self.Tipo = Tipo
        self.Região = Região
    
    def Informações(self):
        lista=[]
        lista.append(self.númeroDex)
        lista.append(self.Espécie)
        lista.append(self.Altura)
        lista.append(self.Peso)
        lista.append(self.Região)
        if len(self.Tipo)!=1:
            tipo=self.Tipo.split("/")
            self.Tipo=tipo[0]+tipo[1]
        lista.append(self.Tipo)
        return lista
    
    def verPokemons(self):
        sql="""
        select * from "Pokedex"
        """
        
        return sql
        