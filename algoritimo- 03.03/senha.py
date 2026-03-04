senha_correta = "123456"
nome = input("digite seu nome: ")

tentativas = 3

while tentativas > 0:
    senha = input("digite sua senha: ")
    
    if senha == senha_correta:
        print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
        break
    else:
        tentativas = 3
        
        if tentativas == 2:
            print(f"senha incorreta! Você ainda tem 2 tentativa!.")
        elif tentativa == 1:
            print("senha incorreta! você tem 1 tentativa!")
        else:
            
            print("sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
