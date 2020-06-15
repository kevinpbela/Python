#Calcular o valor em real e converter em dolar.

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

        real=float(input('Digite o valor em R$ '))

        dolar=float(input('Informe o valor do dolar $ '))

        converter(real,dolar)

        retorno()

    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

    pass

def converter(x,y):

    con=x/y

    print('O valor R$ {:.2f} convertido com o dolar $ {:.2f} é de $ {:.2f}.'.format(x,y,con))

    pass

verificar()