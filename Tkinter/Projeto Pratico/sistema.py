from tkinter import*

janela=Tk()

class Aplicacao():

    def __init__(self):

        self.janela=janela
        self.tela()
        self.frames_de_tela()
        self.botoes()
        janela.mainloop()

        pass

    def tela(self):

        largura=950
        altura=500

        largura_tela=self.janela.winfo_screenwidth()
        altura_tela=self.janela.winfo_screenheight()

        posx=(largura_tela/2)-(largura/2)
        posy=(altura_tela/2)-(altura/2)

        self.janela.title("Cadastro de Cliente")
        self.janela['bg']='#30336b'
        self.janela.geometry('%dx%d+%d+%d'%(largura,altura,posx,posy))
        self.janela.resizable(False,False)
        self.janela.maxsize(width=900,height=700)
        self.janela.minsize(width=400,height=300)

        pass

    def frames_de_tela(self):

        self.frame_1= Frame(self.janela)
        self.frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.45)

        self.frame_2= Frame(self.janela)
        self.frame_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.45)

        pass

    def botoes(self):

        self.btnlimpar=Button(self.frame_1,text='Limpar')
        self.btnlimpar.place(relx=0.01,rely=0.05,relwidth=0.15,relheight=0.20)

        self.btnlimpar=Button(self.frame_1,text='Consultar')
        self.btnlimpar.place(relx=0.01,rely=0.28,relwidth=0.15,relheight=0.20)

        self.btnlimpar=Button(self.frame_1,text='Novo')
        self.btnlimpar.place(relx=0.01,rely=0.52,relwidth=0.15,relheight=0.20)

        self.btnlimpar=Button(self.frame_1,text='Salvar')
        self.btnlimpar.place(relx=0.01,rely=0.74,relwidth=0.15,relheight=0.20)

        pass

    pass

Aplicacao()