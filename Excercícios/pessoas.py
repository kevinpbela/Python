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

        pessoas=[]

        for i in range(1,10+1,1):

            c=int(input('Digite uma à {}º idade: '.format(i)))

            if(c>=18):
                
                pessoas.append(c)

        print('A quantidade de pessoas igual ou maiores de 18 anos é {}.'.format(len(pessoas)))

        retorno()

        pass

    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

        pass

    pass

verificar()