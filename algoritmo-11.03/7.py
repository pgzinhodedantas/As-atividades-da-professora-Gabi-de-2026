
senha = input("digite uma senha: ")

tem_numero = any(c.isdigit() for c in senha)

if len(senha) >= 8 and tem_numero:
    print("senha válida")
else:
    print("senha inválida")