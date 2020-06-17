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
        
        perg=input('Deseja fazer seu pedido?[s/n]: ')

        if(perg=='s' or perg=='S'):

            calcular(perg)

        else:

            print('Cliente seu pedido!')

        retorno()

        pass

    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

        pass

    pass


def calcular(verificar):

    total=list()

    resp=verificar

    while resp=='s' or resp=='S':

        x=float(input('Preço do Produto R$ '))
        y=int(input('Quantidade: '))
        
        total.append(x*y)

        resp=input('Deseja inserir mais um item no pedido?[s/n]: ')

    pedido=sum(total)

    print('O valor total do pedido é de R$ {:.2f}.'.format(pedido))
    
    pass

verificar()