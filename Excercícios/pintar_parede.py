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
        
    except:

        print('Erro - Dados digitados são invalidos!')

        retorno()

    pass

def calcular(x,y):

    res=x*y

    print('Sua parede tem dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(x,y,res))

    print('Para pintar sua parede você vai precisar de {:.2f}L de tinta por m².'.format(res/2))

    pass

verificar()