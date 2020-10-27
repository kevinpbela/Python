def retorno_123():

    resp=input('Deseja executar o programa novamente?[s/n]: ')

    if(resp=='s' or resp=='S'):

        print('#'*30)

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass


def verificar():
    
    try:

        nome=input('Digite seu nome: ')
        faltas=int(input('Digite a quantidade de faltas: '))
        num=int(input('Digite um número maior que 1: '))

        if(num<=1):

            print('O número informado é menor do que foi solicitado!')

            retorno()

        else:

            dados(nome,faltas,num)

            retorno()

        pass
    except:

        print('Erro - Dados invalidos!')

        retorno()

        pass

    pass

def dados(x,y,m):

    nota=list()

    for i in range(1,m+1,1):

        c=float(input('Digite a {}º nota: '.format(i)))
        
        nota.append(c)

    media=sum(nota)/len(nota)

    print('-'*40)

    
    print('Nome: {}'.format(x))
    print('-'*30)
    print('A quantidade de faltas: {}'.format(y))
    print('-'*30)
    print('A média do aluno é {:.2f}'.format(media))
    

    print('-'*40)  

    if(media>=7):

        print('Aluno aprovado!')

    elif(media>=4 and media<7):

        print('Aluno de recuperação!')

    else:

        print('Aluno de reprovado!')

    pass

verificar()
