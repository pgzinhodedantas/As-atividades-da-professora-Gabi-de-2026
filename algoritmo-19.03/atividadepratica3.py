def rank_jogador(pontos, derrotas):
    pontos_finais = pontos - (derrotas * 15)
    
    if pontos_finais < 0:
        return "banido"
    elif pontos_finais < 180:
        return "Bronze"
    elif pontos_finais < 400:
        return "Prata"
    elif pontos_finais < 800:
        return "Ouro"
    else:
        return "Diamante"