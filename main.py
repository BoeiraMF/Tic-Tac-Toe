import jogo as j
import placar as p
import placar as p
from pathlib import Path

# garante a criação do arquivo "score_players.txt"
p.garantir_score()
print("Arquivo de score encontrado com sucesso!")

while True:

    try:
        menu = int(input
        ("""
+---------------------+
|=====TIC TAC TOE=====|
|  1. Jogar           |
|  2. Placar          |
|  3. Créditos        |
|  4. Sair            |
+---------------------+
>>>"""))
    

#------Jogar------
        if menu == 1:
            tabuleiro_jogo = ["0","1","2","3","4","5","6","7","8"]

            j.mapa(tabuleiro_jogo, mostrar = False)    
            j.jogar(tabuleiro_jogo)


#------Placar------
        elif menu == 2:
            p.consultar_score()



#------Créditos------

        elif menu == 3:
            print("""       ===CRÉDITOS===
+--------------------------+
|Feito por: Matheus Boeira |
+--------------------------+""")
            while True:
                voltar_credit = int(input("""\n1 - Volta ao menu
>>>"""))
                if voltar_credit == 1:
                    break
                else:
                    print("Para voltar você precisa digitar (1)!")
                    continue
                    

#------Sair------
        elif menu == 4:
            print("Obrigado por jogar. Volte sempre!")
            break




#------Opção inválida------
        else:
            print("Insira uma opção válida!")
            continue

    except ValueError:
        print("Entrada inválida. Por favor, insira um valor válido!")