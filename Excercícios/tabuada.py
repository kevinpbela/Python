'''
Criar uma tabuada conforme passada pelo usuário.
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

        val=int(input('Digite um valor inteiro: '))

        tabuada(val)

        retorno()

    except:

        print('Erro - Dado fornecido está invalido!')

        retorno()

    pass


def tabuada(x):

    print('=====Tabuada======')

    print('='*30)

    for i in range(0,10+1,1):

        res=i*x

        print('{} x {} = {}'.format(i,x,res))

    print('='*30)
    
    pass

verificar()