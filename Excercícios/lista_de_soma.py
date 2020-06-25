#programa que soma valores passado pelo usuário

def retorno():

    resp=input('Deseja executar o programa novamente?[s/n]: ')

    if(resp=='s' or resp=='S'):

        print('='*30)

        soma()

        pass
    
    else:

        print('Processo finalizado com sucesso!')

        pass
    
    pass

def soma():

    valores=list()

    res='s'

    while(res=='s' or res=='S'):

        try:

            val=float(input('Digite um valor: '))
                        
            pass

        except:

            print('Erro - Dados inserido são invalidos!')

            retorno()

            pass

        valores.append(val)

        res=input('Deseja inserir um novo valor?[s/n] ')

    total=sum(valores)

    print('O total dos valores é {:.2f}.'.format(total))

    retorno()

    pass


soma()