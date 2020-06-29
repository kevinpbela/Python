from tkinter import*

janela=Tk()

class Aplicacao():

    def __init__(self):

        self.janela=janela
        self.tela()
        self.frames_de_tela()
        janela.mainloop()

        pass

    def tela(self):

        self.janela.title("Cadastro de Cliente")
        self.janela['bg']='#30336b'
        self.janela.geometry('750x500+0+0')
        self.janela.resizable(True,True)
        self.janela.maxsize(width=900,height=700)
        self.janela.minsize(width=400,height=300)

        pass

    def frames_de_tela(self):

        self.frame_1= Frame(self.janela)
        self.frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.45)

        self.frame_2= Frame(self.janela)
        self.frame_2.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.45)

        pass

    pass

Aplicacao()