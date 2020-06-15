'''
Pegar o nome do usuário, idade e peso e mostrar na tela.
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

        nome=str(input('Digite seu nome: '))
        idade=int(input('Digite sua idade: '))
        peso=float(input('Digite seu peso: '))

        print('Meu nome é {} e tenho {} anos e peso {:.2f}.'.format(nome,idade,peso))

        retorno()

    except:

        print('Erro - Dados digitados não são valores validos!')

        retorno()

    pass

verificar()