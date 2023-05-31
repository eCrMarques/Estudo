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

        entry=[]
        entry.append(CTkEntry(self,70,20,fg_color="white",placeholder_text="Nome"))
        entry[0].grid(pady=2,padx=5,column=0,row=1,sticky="w")
        entry.append(CTkEntry(self,80,20,fg_color="white",placeholder_text="Nome"))
        entry[1].grid(pady=2,padx=5,column=1,row=1,sticky=EW)
        entry.append(CTkEntry(self,70,20,fg_color="white",placeholder_text="Nome"))
        entry[2].grid(pady=2,padx=5,column=2,row=1,sticky="e")

        self.quantidade=0
        self.destroir=None
        self.master=master
        self.JanelaCompra=None
        
        # Compras
        self.status=None
        self.compras=[]
        self.item=[]
        for tabela in entry:
            tabela.bind("<Return>", lambda e: self.adicionarTabela(entry)) 

    def destruirTabela(self,Tables,All=False,pos=None):
        if self.destroir==None:
            self.destroir=CTkFrame(self,20,20,bg_color="gray",fg_color="red",corner_radius=10)
            print(self.quantidade)
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
            if len(produtos)>1:
                mudar=False
                for produto in produtos:
                    if produto==prevTabela:
                        mudar=True
                        produtos.remove(produto)
                    elif mudar:
                        produto[0].grid(row=pos)
                        produto[1].grid(row=pos)
                        produto[2].grid(row=pos)
                        pos+=1
                        


    def adicionarTabela(self,tabela):
        global produtos
        global posLinha
        posLinha+=1
        entrada=True
        for item in tabela:
            if item.get()=='':
                entrada=False
        if entrada and (tabela[2].get()).isnumeric():
            Tabela=[]
            for i,item in enumerate(tabela):
                if i==2:
                    posItem=posLinha
                Tabela.append(CTkLabel(self,text=f"{item.get()}",font=CTkFont(size=15)))
                Tabela[i].grid(pady=2,padx=5,column=i,row=posLinha,sticky="w")
                Tabela[i].bind("<Button-1>", lambda index: (self.destruirTabela(Tabela,pos=posLinha),self.AtualizarCompra((posItem,Tabela))))
            produtos.append(Tabela)

    def AtualizarCompra(self,pos):
        try:
            if self.Dados!=[item.cget("text") for item in pos[1]]:
                self.item.append(f'{self.Dados[0]}--{self.quantidade}')
                print(self.item)
        except:pass
        self.Dados=[item.cget("text") for item in pos[1]]
        print(self.Dados)
        if self.status==None:
            aumentar=CTkFrame(self,10,10,fg_color="green")
            aumentar.grid(pady=(2,5),column=2,row=pos[0],sticky="en")
            aumentar.bind("<Button-1>", lambda e: self.Comprar("Aumentar"))
            diminuir=CTkFrame(self,10,10,fg_color="red")
            diminuir.grid(pady=(2,5),column=2,row=pos[0],sticky="es")
            diminuir.bind("<Button-1>", lambda e: self.Comprar("Diminuir"))
            self.status=[aumentar,diminuir]
        else:
            for status in self.status:
                status.destroy()
            self.status=None
    def Comprar(self, status):
        match status:
            case "Aumentar":
                self.quantidade+=1
            case "Diminuir":
                self.quantidade-=1
                if self.quantidade<=0:
                    self.quantidade=0
        print(self.quantidade)
        if self.quantidade>0:
            print('Asd')
            if self.JanelaCompra==None:
                Concluir=CTkLabel(self.master,10,10,text=f"{self.quantidade}",fg_color="blue")
                Concluir.place(relx=0.9)
                self.JanelaCompra=Concluir
                Concluir.bind("<Button-1>", lambda e:(self.EfetuarCompra(f"{self.Dados[0]} - {self.quantidade}")))

            self.JanelaCompra.configure(text=f'{self.quantidade}')
        elif self.quantidade<=0:
            print('asd')
            self.JanelaCompra.destroy()
            self.JanelaCompra=None

    def EfetuarCompra(self,item):
        self.item.append(item)
        print(self.item)
        self.item=[]
        try:
            self.JanelaCompra.destroy()
            self.JanelaCompra=None
            for status in self.status:
                status.destroy()
            self.status=None
            self.destroir.destroy()
            self.destroir=None
            self.quantidade=0
        except:pass

produtos=[]
posLinha=1


app = App()
app.mainloop()