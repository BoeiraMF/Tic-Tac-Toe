import random

def mapa (tabuleiro, mostrar = True):

    if mostrar:
        print(" " + "_____" + " " + " " + "_____" + " " + " " + "_____" + " " )
        print("|" + " " * 5 + "|" + "|" + " " * 5 + "|" + "|" + " " * 5 + "|")
        print(f"|  {tabuleiro[0]}  ||  {tabuleiro[1]}  ||  {tabuleiro[2]}  |")
        print("|" + "_" * 5 + "|" + "|" + "_" * 5 + "|" + "|" + "_" * 5 + "|")
        print("|" + " " * 5 + "|" + "|" + " " * 5 + "|" + "|" + " " * 5 + "|")
        print(f"|  {tabuleiro[3]}  ||  {tabuleiro[4]}  ||  {tabuleiro[5]}  |")
        print("|" + "_" * 5 + "|" + "|" + "_" * 5 + "|" + "|" + "_" * 5 + "|")
        print("|" + " " * 5 + "|" + "|" + " " * 5 + "|" + "|" + " " * 5 + "|")
        print(f"|  {tabuleiro[6]}  ||  {tabuleiro[7]}  ||  {tabuleiro[8]}  |")
        print("|" + "_" * 5 + "|" + "|" + "_" * 5 + "|" + "|" + "_" * 5 + "|")
    return tabuleiro


def cadastro():
    player1 = input("Insira o nome do jogador 1 (X): ")
    player2 = input("Insira o nome do jogador 2 (O): ")

    return player1, player2
 

def vitoria(tabuleiro):
    combinacao_vitoria = [
      # Linhas
      (0, 1, 2),
      (3, 4, 5),
      (6, 7, 8),
      # Colunas
      (0, 3, 6),
      (1, 4, 7),
      (2, 5, 8),
      # Diagonais
      (0, 4, 8),
      (2, 4, 6),
    ]

    for a, b, c in combinacao_vitoria:
        # Checa se as três posições têm o mesmo símbolo (X ou O)
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return tabuleiro[a]  # Retorna o símbolo vencedor ('X' ou 'O')

    return None  # Retorna None se ninguém ganhou ainda
    


def jogar(tabuleiro):
    player1, player2 = cadastro()

    jogador_atual = random.randint(1,2)
    segunda_jogada = 0
    jogada_feita = []
    turnos = 0


    if jogador_atual == 1:
        print(f"Jogador {player1} começa (X)!\n")
        mapa(tabuleiro)

    elif jogador_atual == 2:
        print(f"Jogador {player2} começa (O)!\n")
        mapa(tabuleiro)

    while turnos != 9:
        try:
            jogada = int(input("\nEscolha um local vazio para jogar! (0 a 8): "))

            if jogada >= 0 and jogada <=8:
                if jogada in jogada_feita:
                    print("\nCasa já escolhida. Por favor tente outra!")
                    mapa(tabuleiro)
                    continue

                if jogador_atual == 1:
                    tabuleiro[jogada] = "X"
                    mapa(tabuleiro)
                    jogada_feita.append(jogada)
                    turnos +=1

                    if vitoria(tabuleiro):
                        print(f"\nParabéns! {player1} GANHOU O JOGO!!!!")
                        break

                    jogador_atual = 2

                elif jogador_atual == 2:
                    tabuleiro[jogada] = "O"
                    mapa(tabuleiro)
                    jogada_feita.append(jogada)
                    turnos +=1

                    if vitoria(tabuleiro):
                        print(f"\nParabéns! {player2} GANHOU O JOGO!!!!")
                        break

                    jogador_atual = 1

            else:
                print("\nEscolha uma opção válida!")
                mapa(tabuleiro)
                continue

        except ValueError:
            print("\nInsira somente números!")
            mapa(tabuleiro)

    if turnos == 9 and not vitoria(tabuleiro):
        print("\nDeu velha. Foi um empate! :(")