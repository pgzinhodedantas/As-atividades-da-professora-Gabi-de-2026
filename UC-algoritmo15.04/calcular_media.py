def calcular_media():
    notas = []
    
    try:
        for i in range(3):
            nota = float(input(f"Digite a {i+1}ª nota: "))
            notas.append(nota)
        
        media = sum(notas) / 3
        print(f"Média final: {media:.2f}")
    
    except ValueError:
        print("Erro: as notas devem ser numéricas.")