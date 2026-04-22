produtos = []

def menu():
    print("\n=== SISTEMA MOVRA ===")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Editar Produto")
    print("5 - Excluir Produto")
    print("6 - Gerar Relatório")
    print("7 - Opção Extra")
    print("0 - Sair")

def cadastrar_produto():
    print("\n=== CADASTRAR PRODUTO ===")
    try:
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço: ").replace(",", "."))
        quantidade = int(input("Quantidade: "))
        if nome == "" or preco < 0 or quantidade < 0:
            print("Valores inválidos.")
            return
    except ValueError:
        print("Erro: digite valores numéricos válidos!")
        return

    produto = {
        "id": len(produtos) + 1,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    print("\n=== LISTA DE PRODUTOS ===")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Quantidade: {p['quantidade']}")
def buscar_produto():
    termo = input("Digite o nome ou ID do produto para buscar: ").strip()
    encontrados = []
    if termo.isdigit():
        for p in produtos:
            if p['id'] == int(termo):
                encontrados.append(p)
    else:
        for p in produtos:
            if termo.lower() in p['nome'].lower():
                encontrados.append(p)
    if encontrados:
        for p in encontrados:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Quantidade: {p['quantidade']}")
    else:
        print("Produto não encontrado.")

def editar_produto():
    try:
        id_editar = int(input("Digite o ID do produto para editar: "))
    except ValueError:
        print("ID inválido!")
        return
    for p in produtos:
        if p['id'] == id_editar:
            print(f"Editando {p['nome']}")
            novo_nome = input(f"Novo nome [{p['nome']}]: ").strip() or p['nome']
            try:
                novo_preco = input(f"Novo preço [{p['preco']}]: ").replace(",", ".")
                novo_preco = float(novo_preco) if novo_preco else p['preco']
                nova_qtd = input(f"Nova quantidade [{p['quantidade']}]: ")
                nova_qtd = int(nova_qtd) if nova_qtd else p['quantidade']
            except ValueError:
                print("Valores inválidos!")
                return
            p['nome'] = novo_nome
            p['preco'] = novo_preco
            p['quantidade'] = nova_qtd
            print("Produto atualizado!")
            return
    print("Produto não encontrado.")

def excluir_produto():
    try:
        id_excluir = int(input("Digite o ID do produto para excluir: "))
    except ValueError:
        print("ID inválido!")
        return
    for i, p in enumerate(produtos):
        if p['id'] == id_excluir:
            print(f"Excluindo {p['nome']}...")
            del produtos[i]
            print("Produto excluído!")
            return
    print("Produto não encontrado.")

def gerar_relatorio():
    print("\n=== RELATÓRIO DE PRODUTOS ===")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    total = sum(p['preco'] * p['quantidade'] for p in produtos)
    print(f"Total em estoque: R${total:.2f}")
    listar_produtos()

def opcao_extra():
    print("\n=== OPÇÃO EXTRA ===")
    print("Um sistema de cadastro de alimentos e produtos é essencial para organização e controle, principalmente quando há muitos itens como alimentos, produtos e produtos higiênicos. Controlar o estoque, organizar produtos, facilitar vendas e saber o que precisa ser reposto!")
while True:
    menu()
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro: digite um número válido!")
        continue
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        buscar_produto()
    elif opcao == 4:
        editar_produto()
    elif opcao == 5:
        excluir_produto()
    elif opcao == 6:
        gerar_relatorio()
    elif opcao == 0:
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")