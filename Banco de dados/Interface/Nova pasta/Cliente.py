from customtkinter import *



class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        
        
        tabela=Tabela(self)

class Tabela(CTkScrollableFrame):
    def __init__(self,master):
        super().__init__(master=master,width=300,height=400)
        self.grid_columnconfigure((0,1,2),weight=1)
        self.grid_rowconfigure((0,1),weight=1)
        self.grid(pady=50,padx=250)

        CTkLabel(self,fg_color="gray",corner_radius=10,text="Produto",font=CTkFont(weight="bold",size=20)).grid(column=0,row=0,padx=5,sticky="ew",columnspan=4)


        pesquisa=CTkEntry(self,70,20,fg_color="white",placeholder_text="Pesquisar")
        self.pesquisa=pesquisa
        self.teste=pesquisa
        pesquisa.grid(pady=2,padx=5,column=0,row=1,columnspan=3,sticky="ew")
        pesquisa.bind("<Return>", lambda e: self.Pesquisar(pesquisa.get())) 
        self.pesquisaCliente=None
        self.destroir=None

        # Adicionar Cliente
        adicionarCliente=CTkFrame(self,25,25,fg_color="blue")
        adicionarCliente.place(relx=0.9)
        adicionarCliente.bind("<Button-1>", lambda e: self.table(pesquisa))
        self.JanelaAdicionar=None

        self.destroir=None
        self.Cliente=[]
    def Pesquisar(self, informação):
        Cliente=False
        if informação !='' and len(informação)>1:
            for cliente in self.Cliente:
                for dados in cliente:
                    if dados.cget("text").lower()==informação.lower():
                        Cliente=True
                        pos=cliente
                        break
            if Cliente==True:
                Tabela=[]
                fundo=CTkFrame(self,height=30,fg_color="green")
                fundo.grid(pady=2,padx=5,column=0,row=2,sticky="ew",columnspan=3)
                self.fundo=fundo
                for i,info in enumerate(pos):

                    nome=info.cget("text")
                    print(i)
                    Tabela.append(CTkLabel(self,text=f'{nome}',font=CTkFont(size=15),bg_color="green",text_color="black"))
                    Tabela[i].grid(pady=2,padx=5,column=i,row=2,sticky="w")
                    self.pesquisaCliente=Tabela
        else:
            for pesquisa in self.pesquisaCliente:
                self.fundo.destroy()
                pesquisa.destroy()


    def table(self,janelaPesquisa):
        if self.JanelaAdicionar== None:
            entry=[]
            entry.append(CTkEntry(self,70,20,fg_color="white",placeholder_text="Nome"))
            entry[0].grid(pady=2,padx=5,column=0,row=1,sticky="w")
            entry.append(CTkEntry(self,80,20,fg_color="white",placeholder_text="Nome"))
            entry[1].grid(pady=2,padx=5,column=1,row=1,sticky=EW)
            entry.append(CTkEntry(self,70,20,fg_color="white",placeholder_text="Nome"))
            entry[2].grid(pady=2,padx=5,column=2,row=1,sticky="e")
            for tabela in entry:
                tabela.bind("<Return>", lambda e: self.adicionarTabela(entry)) 
            self.JanelaAdicionar= entry
            self.pesquisa.destroy()
        else:
            for item in self.JanelaAdicionar:
                item.destroy()
            self.JanelaAdicionar=None
            self.pesquisa=CTkEntry(self,70,20,fg_color="white",placeholder_text="Pesquisar")
            self.pesquisa.grid(pady=2,padx=5,column=0,row=1,columnspan=3,sticky="ew")
            self.pesquisa.bind("<Return>", lambda e: self.Pesquisar(self.pesquisa.get()))

    def destruirTabela(self,Tables,All=False,pos=None):
        if self.destroir==None:
            self.destroir=CTkFrame(self,20,20,bg_color="gray",fg_color="red",corner_radius=10)
            self.destroir.place(x=270,y=0)
            self.destroir.bind("<Button-1>", lambda e:self.destruirTabela(Tables,All=True,pos=pos))
            
        else:
            self.destroir.destroy()
            self.destroir=None
        if All:
            for tabela in Tables:
                prevTabela=Tables
                tabela.destroy()
                pass
            if len(self.Cliente)>1:
                mudar=False
                for produto in self.Cliente:
                    if produto==prevTabela:
                        print('asd')
                        mudar=True
                    elif mudar:
                        produto[0].grid(row=pos)
                        produto[1].grid(row=pos)
                        produto[2].grid(row=pos)
                        pos+=1
            self.Cliente.remove(Tables)


    def adicionarTabela(self,tabela):
        print(self.Cliente)
        global posLinha
        posLinha+=1
        entrada=True
        for item in tabela:
            if item.get()=='':
                entrada=False
        if entrada and (tabela[2].get()).isnumeric():
            Tabela=[]
            for i,item in enumerate(tabela):
                
                Tabela.append(CTkLabel(self,text=f"{item.get()}",font=CTkFont(size=15)))
                Tabela[i].grid(pady=2,padx=5,column=i,row=posLinha,sticky="w")
                Tabela[i].bind("<Button-1>", lambda e: self.destruirTabela(Tabela,pos=posLinha))
            self.Cliente.append(Tabela)
posLinha=1

app = App()
app.mainloop()