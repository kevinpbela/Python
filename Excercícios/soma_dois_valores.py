'''
Somar dois parâmetros passado pelo usuário e apresentar o resultado na tela.
'''

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

        val1=float(input('Digite um valor: '))
        val2=float(input('Digite um valor: '))

        res=soma(val1,val2)

        print('A soma de {} e {} é igual à {:.2f}.'.format(val1,val2,res))

        retorno()

    except:

        print('Erro - Dados inseridos não são validos!')

        retorno()

    pass


def soma(a,b):

    return a+b

    pass

verificar()