# Sistema do MOVRA 

def menu():
    print("\n=== SISTEMA MOVRA ===")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Editar Produto")
    print("5 - Excluir Produto")
    print("6 - Gerar Relatório")
    print("0 - Sair")

while True:
    menu()
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro: digite um número válido!")
        continue  # para volta ao menu

    if opcao == 1:
        print(">> Cadastrar Produto (em construção)")
    
    elif opcao == 2:
        print(">> Listar Produtos (em construção)")
    
    elif opcao == 3:
        print(">> Buscar Produto (em construção)")
    
    elif opcao == 4:
        print(">> Editar Produto (em construção)")
    
    elif opcao == 5:
        print(">> Excluir Produto (em construção)")
    
    elif opcao == 6:
        print(">> Gerar Relatório (em construção)")
    
    elif opcao == 0:
        print("Encerrando o sistema...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")

def cadastrar_produtor():
    while True: 
        print("\n=== CADASTRAR PRODUTO ===")

        try:
            nome = input("nome do produto: ").strip()
            preco = float(input("preço: "))
            quantidade = int(input("quantidade:"))

            # validação (Dados validos?)
            if nome == "" or preco < 0 or quantidade < 0:
                continue 

        except ValueError:
            print("Error: digite valores numéricos válidos!")
            continue


        # Dados válidos → salvar produto
        produto = {
            "id": len(produto) + 1,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produto.items(produto)
        print("Produto cadastrado com sucesso!")