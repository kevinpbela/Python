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
        
        val=float(input('Digite seu salário atual R$ '))

        calcular(val)

        retorno()

        pass

    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

        pass

    pass

def calcular(x):

    res=x*((100+15)/100)

    print('O salário anterior era de R$ {:.2f} e você teve um aumento de 15%, ficando no salário novo de R$ {:.2f}.'.format(x,res)) 

    pass

verificar()