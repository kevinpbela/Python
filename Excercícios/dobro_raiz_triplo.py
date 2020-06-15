'''
Criar um programa que receba o parâmetro o usuário e calcule, o dobro a raiz e o triplo do valor inteiro digitado.
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

        val=int(input('Digite um número inteiro: '))

        calculo(val)

        retorno()

    except:

        print('Erro - Dados digitados são invalidos!')

        retorno()

    pass

def calculo(x):

    dobro(x)
    triplo(x)
    raiz(x)

    pass

def dobro(x):

    res=x*2

    print('O dobro de {} é igual à {}.'.format(x,res))

    pass

def triplo(x):

    res=x*3

    print('O triplo de {} é igual à {}.'.format(x,res))    

    pass

def raiz(x):

    res=x**(1/2)

    print('A raiz quadrada de {} é igual à {:.2f}.'.format(x,res))    

    pass

verificar()