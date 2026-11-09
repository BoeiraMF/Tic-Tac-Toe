from pathlib import Path
import re

arquivo_nome = Path("score_players.txt")

def garantir_score():
    with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
        pass

def cadastrar_jogador(nome_jogador, nome_adversario=None):

    arquivo_path = Path("score_players.txt")
    
    # 1. Validação: Impede que os dois jogadores tenham o mesmo nome na mesma partida
    if nome_adversario and nome_jogador.strip().lower() == nome_adversario.strip().lower():
        print("Os jogadores não podem ter o mesmo nome na mesma partida. Por favor, insira um nome diferente.")
        return False

    # Lê as linhas atuais do arquivo, se ele existir
    linhas = []
    if arquivo_path.exists():
        with open(arquivo_path, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            
    padrao = r"^(.*?)\s*=\s*\{Vitórias:\s*(\d+)\}\s*\{Derrotas:\s*(\d+)\}$"
    
    # 2. Verifica se o jogador já está cadastrado no histórico
    jogador_ja_no_arquivo = False
    for linha in linhas:
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue
            
        match = re.match(padrao, linha_limpa)
        if match:
            nome_atual = match.group(1).strip()
            if nome_atual.lower() == nome_jogador.strip().lower():
                jogador_ja_no_arquivo = True
                break
                
    # Se NÃO estiver no arquivo histórico, cadastra ele zerado.
    # Se JÁ ESTIVER, não faz nada (mantém o placar antigo) e apenas autoriza a partida.
    if not jogador_ja_no_arquivo:
        with open(arquivo_path, "a", encoding="utf-8") as f:
            f.write(f"{nome_jogador.strip()} = {{Vitórias: 0}} {{Derrotas: 0}}\n")
        
    return True  # Nome liberado para prosseguir

def registrar_score(nome_jogador, venceu: bool):
    
    arquivo_path = Path("score_players.txt")
    if not arquivo_path.exists():
        return
        
    with open(arquivo_path, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        
    novas_linhas = []
    padrao = r"^(.*?)\s*=\s*\{Vitórias:\s*(\d+)\}\s*\{Derrotas:\s*(\d+)\}$"
    
    for linha in linhas:
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue
            
        match = re.match(padrao, linha_limpa)
        
        if match:
            nome_atual = match.group(1).strip()
            vitorias = int(match.group(2))
            derrotas = int(match.group(3))
            
            # Localiza o jogador e atualiza o placar correspondente
            if nome_atual.lower() == nome_jogador.strip().lower():
                if venceu:
                    vitorias += 1
                else:
                    derrotas += 1
            
            novas_linhas.append(f"{nome_atual} = {{Vitórias: {vitorias}}} {{Derrotas: {derrotas}}}\n")
        else:
            novas_linhas.append(linha)
            
    # Salva as alterações de placar no arquivo
    with open(arquivo_path, "w", encoding="utf-8") as f:
        f.writelines(novas_linhas)


def consultar_score():
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    if conteudo == '':
        print("\nPLACAR\n")
        print("Placar vazio. Jogue uma partida para registrar uma pontuação!")

    else:
        print("\nPLACAR\n")
        print(conteudo)