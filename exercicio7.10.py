#O exercício pede para fazer um jogo da velha, porém foi feito sem usar funções, uma vez que no capítulo onde esse exercício esta localizado não havia sido ensinado ainda a usar funções.

intro = input("Bem-vindo ao Jogo da Velha! (pressione Enter para começar):")
vez_do_jogador = False
vitoria = False
numero_rodada = 1
l1 = list(" 7 | 8 | 9")
l2 = list(" 4 | 5 | 6")
l3 = list(" 1 | 2 | 3")

if intro == "":
  #Nome dos jogadores e símbolos
    player_1 = input("Insira nome do primeiro jogador (usa X): ")
    player_2 = input("Insira nome do segundo jogador (usa O): ")
  #Comando para pular linha
    for e in range(3):
        print()
    while True:
        cont = 0
        posicao_da_jogada = 0
        simbolo_da_jogada = ""
      #Número da rodada
        print("**{0}o RODADA**".format(numero_rodada))
      #Comando para pular linha
        print()
      #Desenho Jogo da Velha
      #linha = l
        desenho_jogo = [l1, l2, l3] 
        for e in desenho_jogo:
            print("".join(e))
            if cont != 2:
                print("---+---+---")
            cont +=1
      #Comando para pular linha
        print()
      #Mensagem de vitória
        if vitoria == True:
            if vez_do_jogador == True:
                nome_jogador_na_mensagem = player_1
            else:
                nome_jogador_na_mensagem = player_2
            print("***{0} Venceu!!!***".format(nome_jogador_na_mensagem))
            break
      #Mensagem de velha
        if numero_rodada == 10:
            print("***Deu velha, Ninguém venceu!!!")
            break
      #Comando que alterna os jogadores
        vez_do_jogador = not vez_do_jogador
      #Registro da posição
        while posicao_da_jogada not in range(1,10):
            print("Insira uma posição livre de 1 a 9")               
            if vez_do_jogador == True:
                posicao_da_jogada = int(input("{0}, onde deseja jogar ?: ".format(player_1)))
                simbolo_da_jogada = "X"
                print()
            elif vez_do_jogador == False:
                posicao_da_jogada = int(input("{0}, onde deseja jogar ?: ".format(player_2)))
                simbolo_da_jogada = "O"
                print()
          #Verificação da posição
            if posicao_da_jogada == 1 or 2 or 3:
                if posicao_da_jogada == 1:
                    if l3[1] != "1":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l3[1] = "{0}".format(simbolo_da_jogada)
                        break
                elif posicao_da_jogada == 2:
                    if l3[5] != "2":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l3[5] = "{0}".format(simbolo_da_jogada)
                        break        
                elif posicao_da_jogada == 3:
                    if l3[9] != "3":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l3[9] = "{0}".format(simbolo_da_jogada)
                        break        
            if posicao_da_jogada == 4 or 5 or 6:
                if posicao_da_jogada == 4:
                    if l2[1] != "4":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l2[1] = "{0}".format(simbolo_da_jogada)
                        break
                elif posicao_da_jogada == 5:
                    if l2[5] != "5":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l2[5] = "{0}".format(simbolo_da_jogada)
                        break        
                elif posicao_da_jogada == 6:
                    if l2[9] != "6":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l2[9] = "{0}".format(simbolo_da_jogada)
                        break
            if posicao_da_jogada == 7 or 8 or 9:
                if posicao_da_jogada == 7:
                    if l1[1] != "7":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l1[1] = "{0}".format(simbolo_da_jogada)
                        break
                elif posicao_da_jogada == 8:
                    if l1[5] != "8":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l1[5] = "{0}".format(simbolo_da_jogada)
                        break        
                elif posicao_da_jogada == 9:
                    if l1[9] != "9":
                        print("--> Essa posição já está ocupada <--")
                        print()
                        posicao_da_jogada = 0
                        continue
                    else:
                        l1[9] = "{0}".format(simbolo_da_jogada)
                        break
      #Verificação de vitória
        if vitoria == False:
            if l3[1] == l3[5] and l3[1] == l3[9]: #1,2,3
                vitoria = True
            elif l2[1] == l2[5] and l2[1] == l2[9]: #4,5,6
                vitoria = True
            elif l1[1] == l1[5] and l1[1] == l1[9]: #7,8,9
                vitoria = True
            elif l3[1] == l2[1] and l3[1] == l1[1]: #1,4,7
                vitoria = True
            elif l3[5] == l2[5] and l2[5] == l1[5]: #2,5,8
                vitoria = True
            elif l3[9] == l2[9] and l3[9] == l1[9]: #3,6,9
                vitoria = True
            elif l3[1] == l2[5] and l3[1] == l1[9]: #1,5,9
                vitoria = True
            elif l3[9] == l2[5] and l3[9] == l1[1]: #3,5,7
                vitoria = True
        numero_rodada += 1