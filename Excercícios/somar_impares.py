def retorno():

    resp=input('Deseja executar o programa novamente?[s/n]: ')

    if(resp=='s' or resp=='S'):

        print('#'*30)

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass

def verificar():

    try:

        nu1=int(input('Digite um valor inicial: '))
        nu2=int(input('Digite uma sequência: '))

        lista(nu1,nu2)

        retorno()

        pass

    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

        pass

    pass

def lista(x,y):

    num=[]

    for i in range(x,y+1,1):

        if(i%2!=0):

            num.append(i)

    soma=sum(num)
    qtde=len(num)

    print('Na lista contém {} números ímpares e a soma é {}.'.format(qtde,soma))
    #retorno()

    pass

verificar()