'''
Pegar um número inteiro e calcular o antecessor e o sucessor.
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

        print('O número digitado é {} o antecessor é {} e o sucessor é {}.'.format(val,val-1,val+1))

        retorno()

    except:

        print('Erro - Dados inseridos não são validos!')

        retorno()

    pass

verificar()