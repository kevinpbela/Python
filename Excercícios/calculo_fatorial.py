def calcular(x):

    calc=1

    for i in range(x,0,-1):

        calc*=i

    print('O valor fatorial de {} é {}.'.format(x,calc))

    pass

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

        nu1=int(input('Digite um valor inteiro: '))

        calcular(nu1)

        retorno()

        pass

    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

        pass

    pass

verificar()