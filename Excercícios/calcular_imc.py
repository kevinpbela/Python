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

        altura=float(input('Informe sua altura: '))
        peso=float(input('Informe seu peso: '))

        calc_imc(peso,altura)

        retorno()

        pass

    except:

        print('Erro - Dados invalidos!')

        retorno()

        pass

    pass

def calc_imc(a,b):

    valor=a/(b*b)

    if(valor<18.5):

        print('Abaixo do peso. Seu IMC é {:.2f}.'.format(valor))

    elif(valor>=18.6 and valor<=24.9):

        print('Peso ideal. Seu IMC é {:.2f}.'.format(valor))

    else:

        print('Acima do peso. Seu IMC é {:.2f}.'.format(valor))

    pass

verificar()