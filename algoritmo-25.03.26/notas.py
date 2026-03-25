def resumo_notas(notas):
    if not notas:
        return "Lista vazia"
    
    for n in notas:
        if not isinstance(n, (int, float)):
           "Erro: todas as notas devem ser números" 
    
    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)

    return {
        "soma": soma,
        "media": media,
        "maior": maior,
        "menor": menor
    }
