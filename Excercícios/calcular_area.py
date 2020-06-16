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
        largura=float(input('Digite a largura: '))
        comprimento=float(input('Digite o comprimento: '))

        calcular(largura,comprimento)

        retorno()

        pass
    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()
        
        pass

    pass

def calcular(a,l):

    res=a*l

    if(a==l):

        print('O quadrado tem área {:.2f}m².'.format(res))

    else:

        print('O retângulo tem área {:.2f}m².'.format(res))
    
    pass

verificar()