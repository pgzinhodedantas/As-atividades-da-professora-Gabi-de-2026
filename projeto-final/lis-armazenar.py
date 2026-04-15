Produtos = []

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