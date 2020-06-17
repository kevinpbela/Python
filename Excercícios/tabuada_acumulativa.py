'''
Criar uma tabuada acumulativa conforme os parâmetros do usuário.
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
        num=int(input('Digite a primeira sequência: '))

        calcular(val,num)

        retorno()

        pass

    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

        pass

    pass


def calcular(x,y):

    cont=list()

    for i in range(y,x+1,1):

        cont.append(i)

        if(len(cont)<=1):

            res=x*i
            memoria=res
            anterior=memoria

            print('{}x{}={}'.format(i,x,res))

            pass

        else:

            res=memoria*i
            anterior=memoria
            memoria=res

            print('{}x{}={}'.format(i,anterior,res))           


    pass


verificar()