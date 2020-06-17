'''
Faça um programa que mostre uma lista de função e calcule conforme a opção escolhida pelo usuário.
'''

def retorno():

    resp=input('Deseja executar o programa novamente?[s/n]: ')

    if(resp=='s' or resp=='S'):

        print('#'*30)

        lista()

    else:

        print('Processo finalizado com sucesso!')

pass


def lista():

    try:


        print('============Menu===============')
        print('1 - Soma\n2 - Divisão\n3 - Multiplicação\n4 - Subtração\n5 - Tabuada')
        print('='*32)
        resp=int(input('Digite uma opção: '))

        funcao={1:soma,2:divisao,3:multiplicacao,4:subtracao,5:tabuada}

        funcao.get(resp)()

        retorno()

    except:

        print('Erro - Dados inserido são invalidos!')

        retorno()

pass

def soma():

    a=float(input('Digite um valor: '))
    b=float(input('Digite um valor: '))

    res=a+b

    print('A soma de {} e {} é igual à {}.'.format(a,b,res))

pass


def divisao():

    a=float(input('Digite um valor: '))
    b=float(input('Digite um valor: '))

    res=a/b

    print('A divisão de {} e {} é igual à {}.'.format(a,b,res))  

pass

def multiplicacao():

    a=float(input('Digite um valor: '))
    b=float(input('Digite um valor: '))

    res=a*b

    print('A multiplicação de {} e {} é igual à {}.'.format(a,b,res))

pass

def subtracao():

    a=float(input('Digite um valor: '))
    b=float(input('Digite um valor: '))

    res=a-b

    print('A subtração de {} e {} é igual à {}.'.format(a,b,res))

pass

def tabuada():

    a=int(input('Digite um valor: '))

    for i in range(0,11,1):

        res=i*a

        print('{}x{}={}'.format(i,a,res))

pass

lista()