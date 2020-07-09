from tkinter import*

cor='#dde'

janela=Tk()

janela.title('form01')
janela.geometry('250x150+0+0')
janela['bg']=cor

lbvalor01=Label(janela,text='Valor 01:',background=cor)
lbvalor02=Label(janela,text='Valor 02:',background=cor)

lbvalor01.place(x=10,y=10)
lbvalor02.place(x=10,y=45)

txvl01=Entry(janela).place(x=65,y=10)
txvl02=Entry(janela).place(x=65,y=45)

btnsoma=Button(janela,text='Somar',command=lambda:print(txvl01.get())).place(x=65,y=75)

lbvalor03=Label(janela,text='Mensagem',width=25,background=cor)
lbvalor03.place(x=25,y=120)

janela.mainloop()


def soma(a,b):

    return a+b

    pass