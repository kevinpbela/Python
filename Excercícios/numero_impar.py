def retorno():

    resp=input('Deseja executar o programa novamente?[s/n]: ')

    if(resp=='s' or resp=='S'):

        print('#'*30)

        calculo()

    else:

        print('Processo finalizado com sucesso!')

    pass

def calculo():

    x=int(input('Digite um valor ímpar: '))

    while x%2==0:
        
        x=int(input('Digite um valor ímpar: '))

    print('Processo finalizado número digitado {}.'.format(x))
        
    pass

calculo()