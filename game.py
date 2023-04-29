import os
import sys
from functions import confereNome, limpaTela, menuEscolhas, jogar, escolhaPalavra, jogo, indicaPalavra, erros, derrota, vitoria, historico, restart
import datetime

iniciar = 1

while iniciar == 1:
    limpaTela()
    input('****** BEM-VINDO AO JOGO DA FORCA ****** \n Criadores: Pedro Bortoli (RA: 1129494) e Stefano Mossi (RA: 1131685) \n Pressione Enter para continuar...')
    input('\n \n ***** REGRAS ***** \n1. O desafiante deve adivinhar a palavra escolhida pelo competidor.')
    input('2. O desafiante terá 3 dicas escolhidas pelo competidor e poderá errar até 5 letras.')
    input('3. Se o desafiante acertar a palavra, ele ganha. Se ele errar, o competidor ganha.')
    desafiante = confereNome('Desafiante')
    competidor = confereNome('Competidor')
    desafianteNome = 'Desafiante ' + desafiante
    competidorNome = 'Competidor ' + competidor
    competidorVencedor = 0
    desafianteVencedor = 0
    horario = datetime.datetime.now()
    horarioStr = horario.strftime("%d/%m/%Y %H:%M:%S")
    limpaTela()
    descoberto = []

    palavra = escolhaPalavra()

    dica1 = input('Dica 1: ')
    dica2 = input('Dica 2: ')
    dica3 = input('Dica 3: ')
    contadorDica = 0 
    erro = 0
    contador = 0
    limite = False
    limpaTela()

    acerto = False
    e = False

    for z in range(0, len(palavra)):
        descoberto.append('_')
    while acerto == False:
        print('Erros: ',contador)
        print('A palavra é: ')
        print(descoberto)
        print('Ela possui',len(palavra), 'letras.')
        print('')
        escolha = menuEscolhas()
        if escolha == '2':
            contadorDica = contadorDica + 1
            if contadorDica == 1:
                limpaTela()
                print('Dica 1: ', dica1)
                print("")
                indicaPalavra(descoberto,palavra,contador)
                print('')
                tentativa = jogar()
                contador = contador + jogo(tentativa,palavra,descoberto)
                limpaTela()
                if contador == 5:
                    limite = 1
                    break
                if descoberto == palavra:
                    acerto = True
                    break
            elif contadorDica == 2:
                limpaTela()
                print('Dica 2: ', dica2)
                print('')
                indicaPalavra(descoberto,palavra,contador)
                print('')
                tentativa = jogar()
                contador = contador + jogo(tentativa,palavra,descoberto)
                limpaTela()
                if contador == 5:
                    limite = 1
                    break
                if descoberto == palavra:
                    acerto = True
                    break
            elif contadorDica == 3:
                limpaTela()
                print('Dica 3: ', dica3)
                print("")
                indicaPalavra(descoberto,palavra,contador)
                print('')
                tentativa = jogar()
                contador = contador + jogo(tentativa,palavra,descoberto)
                limpaTela()
                if contador == 5:
                    limite = 1
                    break
                if descoberto == palavra:
                    acerto = True
                    break
            else:
                limpaTela()
                print('Você não possui mais dicas!')
                print('')
                indicaPalavra(descoberto,palavra,contador)
                print('')
                tentativa = jogar()
                contador = contador + jogo(tentativa,palavra,descoberto)
                limpaTela()
                if contador == 5:
                    limite = 1
                    break
                if descoberto == palavra:
                    acerto = True
                    break
        elif escolha == "1":
            limpaTela()
            indicaPalavra(descoberto,palavra,contador)
            print('')
            tentativa = jogar()
            contador = contador + jogo(tentativa,palavra,descoberto)
            limpaTela()
            if contador == 5:
                limite = 1
                break
            if descoberto == palavra:
                acerto = True
                break
    if acerto == True:
        limpaTela()
        print(competidorNome,'você venceu!')
        print('')
        competidorVencedor = 1
        palavra = str(palavra)
        print('Histórico de partidas:')
        historico(horarioStr, competidorVencedor, palavra, competidorNome, desafianteNome)
        fim = restart()
        if fim == 1:
            limpaTela()
            pass
        else:
            iniciar = 0
            limpaTela()
    if limite == 1:
        limpaTela()
        print(desafianteNome,'você venceu!')
        print('')
        desafianteVencedor = 1
        palavra = str(palavra)
        print('Histórico de partidas:')
        historico(horarioStr, desafianteVencedor, palavra, desafianteNome, competidorNome)
        fim = restart()
        if fim == 1:
            limpaTela()
            pass
        else:
            iniciar = 0
            limpaTela()