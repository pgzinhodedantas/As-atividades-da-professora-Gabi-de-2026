senha_correta = "123456"
nome = input("digite seu nome: ")

tentativas = 3

while tentativas > 0:
    senha = input("digite sua senha: ")
    
    if senha == senha_correta:
        print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
        break
    else:
        tentativas -= 1
        
        if tentativas > 0:
            print(f"senha incorreta! Você ainda tem {tentativas} tentativa(s).")
        else:
            print("sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")