from customtkinter import *

app= CTk()

app.geometry("800x600")
app.title("Primeiro")

app.grid_columnconfigure((0,1,2),weight=1)

def inserirt():
    texto=inserir.get()
    teste.configure(text=texto)
tituloTopo=CTkLabel(app,text="Ola Mundo",text_color='red',font=CTkFont(size=36,weight="bold"))
tituloTopo.grid(row=0,column=0,pady=20,padx=20)

corpoTexto=CTkLabel(app,text="Adeus Mundo",text_color="red",font=CTkFont(size=26,weight="bold"))
corpoTexto.grid(row=0,column=2,pady=20,padx=20)

teste=CTkLabel(app,text="Teste",text_color="red",font=CTkFont(size=26,weight="bold"))
teste.grid(row=0,column=1,pady=20,padx=20)

inserir=CTkEntry(app,placeholder_text="Digite uma nova mensagem")
inserir.grid(row=1,column=1,pady=20,padx=20)

button=CTkButton(app,bg_color="blue",text="Enviar",command=inserirt)
button.grid(row=1,column=3,padx=20,pady=20)


frame=CTkFrame(app,fg_color="purple")
frame.grid(row=2,column=0,padx=0)

btn=CTkButton(app,30,30,text="Teste",bg_color="red").place(x=0,y=0)

app.mainloop()