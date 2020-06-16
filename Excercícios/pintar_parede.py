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



    except:

        print('Erro - Dados digitados são invalidos!')

        retorno()

    pass

def calcular(x,y):

    res=x*y

    print('Sua parede tem dimensão de {}x`{} e sua área é de {}m².'.format(x,y,res))

    print('Para pintar sua parede você vai ')

    pass

verificar()