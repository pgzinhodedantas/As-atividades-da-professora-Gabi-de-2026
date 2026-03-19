def pontuacao_total(pontos, tempo):
    pontos_finais = pontos
    
    if tempo < 30:
        pontos_finais += 50
    elif tempo > 100:
        pontos_finais -= 20
    
    if pontos_finais > 200:
        return "Recorde"
    else:
        return pontos_finais