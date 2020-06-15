'''
Pegar 4 notas digitada pelo usuário e calcular a média e mostrar se o aluno foi aprovado, recuperação ou reprovado.
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

        val=int(input('Digite um valor acima de 1: '))

        if(val<=1):

            print('A quantidade de número informado não é valida!')

            retorno()

        else:

            media(val)

            retorno()

    except:

        print('Erro - Dados digitados são invalidos!')

        retorno()

    pass

def media(x):

    valores=list()

    for i in range(1,x+1,1):

        c=float(input('Digite a {}º nota: '.format(i)))

        valores.append(c)

    res=sum(valores)/len(valores)

    if(res>=7):

        print('Aluno aprovado sua média é {:.2f}.'.format(res))

    elif(res>=4 and res<7):

        print('Aluno de recuperação sua média é {:.2f}'.format(res))

    else:

        print('Aluno reprovado sua média é {:.2f}'.format(res))
    
    pass

verificar()