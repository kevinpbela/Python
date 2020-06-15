def retorno():

    resp=input('Deseja exexutar o programa novamente?[s/n]: ')

    if(resp=='s' or resp=='S'):

        print('#'*30)

        mensagem()

    else:

        print('Processo finalizado!')

    pass

def mensagem():

    print('Olá Mundo!')

    retorno()

    pass

mensagem()