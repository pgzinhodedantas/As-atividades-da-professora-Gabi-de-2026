def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def exibir_menu():
    print("\n=== CALCULADORA SIMPLES ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def obter_numeros():
    try:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("Erro: digite números válidos!")
        return None, None

def calculadora():
    while True:
        exibir_menu()
        opcao = input("escolha uma opção: ")
        
        if opcao == "5":
            print("Até logo!")
            break
        elif opcao in ["1", "2", "3", "4"]:
            num1, num2 = obter_numeros()
            
            if opcao == "1":
                resultado = soma(num1, num2)
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcao == "2":
                resultado = subtracao(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcao == "3":
                resultado = multiplicacao(num1, num2)
                print(f"Resultado: {num1} x {num2} = {resultado}")
            elif opcao == "4":
                resultado = divisao(num1, num2)
                print(f"Resultado: {num1} ÷ {num2} = {resultado}")
        else:
            print("Opção inválida! Escolha entre 1 e 5.")
