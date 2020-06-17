#Calcular o desconto de um valor passado pelo usuário.

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

        val=float(input('Qual é o valor do produto R$ '))

        calcular(val)

        retorno()

        pass
    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

        pass


    pass


def calcular(x):

    res=x*((100-(5))/100)

    print('O valor do produto sem desconto é R${:.2f} e teve um desconto 5%, ficando no valor de R${:.2f}'.format(x,res))

    pass

verificar()