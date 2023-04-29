import os 
import sys

def limpaTela():
    os.system('cls')

def confereNome(jogador):
    while True:
        nome = input(f'Insira o nome do {jogador}: ').strip()
        if not nome:
            print('O nome não pode estar em branco. Por favor, insira um nome válido.')
        else:
            return nome


def menuEscolhas():
    print('(1) Jogar (2) Solicitar dica')
    x = input()
    return x

def jogar():
    while True:
        try:
            letra = input('Tente uma letra: ')
            letraFinal = letra.upper()
            if len(letraFinal) > 1 or len(letraFinal) == 0:
                print('Você precisa inserir uma letra!')
                pass
            else:
                return letraFinal
            break
        except:
            pass

def escolhaPalavra():
    while True:
        palavra = input('Informe a palavra secreta: ')
        palavraFinal = palavra.upper()
        if len(palavraFinal) == 0:
            print('Você precisa inserir uma palavra!')
        elif not palavraFinal.isalpha():
            print('A palavra deve conter apenas letras!')
        elif ' ' in palavraFinal:
            print('A palavra não pode conter espaços em branco!')
        else:
            palavraChave = []
            for letra in palavraFinal:
                if not letra.isdigit():
                    letra.upper()
                    palavraChave.append(letra)
            return palavraChave

def palavraEscondida(x):
    print('A palavra é:', '_'*len(x))
    print('Ela possui', len(x),'letras.')
    print('')

def tamanhoPalavra(x):
    y = '_'*len(x)
    return y

def jogo(x,y,z):
    erro = 0
    aux = 0
    for i in range(0, len(y)):
        if x == y[i]:
            z[i] = x
            aux = 1
    if aux == 0:
        return erro + 1
    else:
        return 0

def indicaPalavra(x,y,erro):
    print('Erros: ',erro)
    print('A palavra é:')
    print(x)
    print('Ela possui',len(y), 'letras.')

def erros(x,y):
    x = x + 1
    if x == 6:
        y = 1
        return y
    else:
        pass

def derrota(x,y):
    if x == True:
        print(y,'você venceu!')
        finalizar = input()

def vitoria(x,y):
    z = 0
    if x == y:
        z = 1
        return z

def historico(u, v, x, y, z):
    if v == 1:
        try:
            arquivo = open('historico.txt','r')
        except FileNotFoundError:
            arquivo = open('historico.txt','w')
        
        historico = arquivo.readlines()
        historico.append('Horário: ')
        historico.append(u)
        historico.append(' Palavra: ')
        historico.append(x)
        historico.append(' Vencedor: ')
        historico.append(y)
        historico.append(' Perdedor: ')
        historico.append(z)
        historico.append('\n')
        
        arquivo.close()  
        arquivo = open('historico.txt', 'w') 
        arquivo.writelines(historico)

        arquivo.close() 
        arquivo = open('historico.txt','r')
        texto = arquivo.readlines()
        for line in texto:
            print(line)
        arquivo.close()

def restart():
    while True:
        try:
            x = 0
            x = int(input('(1) Jogar novamente (2) Sair \n'))
            if x == 1 or x == 2:
                return x
                break
            else:
                print('Insira um valor válido!')
                print('')
        except:
            print('Insira um valor válido!')
            print('')