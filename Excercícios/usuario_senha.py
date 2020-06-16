def retorno():

    resp=input('Deseja executar o programa novamente?[s/n]: ')

    if(resp=='s' or resp=='S'):

        print('#'*30)

        pergunta()

    else:

        print('Processo finalizado com sucesso!')

    pass


def pergunta():

    user=input('Digite seu usuário: ')
    senha=input('Digite sua senha: ')    

    while user!='user' and senha!='senha123':

        user=input('Digite seu usuário: ')
        senha=input('Digite sua senha: ')
        
    print('Seja bem vindo {}.'.format(user))

    retorno()

    pass

pergunta()