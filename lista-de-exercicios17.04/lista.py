print("Hello, world!")

#eleição escolar se pode ou não votar
idade = int(input("digite sua idade"))
if idade >= 16: 
    print("pode votar")
else:
    print("Ainda não pode votar")

#soma de valores
total = 0
while True:
    valor = float(input("digite o valor( 0 para parar): "))
    if valor == 0:
        break
    total += valor

print("total:", total)

#função de imc
def calcular_imc():
    try:
        peso = float(input("digite o peso:"))
        altura = float(input("diigte a altura:"))

        imc = peso / (altura ** 2)

        if imc < 18.5:
            print("magro")
        elif imc <= 24.9:
            print("normal")
        else:
            print("Acima dom peso")
    except:
        print("Entrada inválida")
calcular_imc

#lista de amigos impar e par
print("fabricio, artur, thiago, pedro")

quantidade = len()

if quantidade % 2 == 0:
    print("Quantidade par:", quantidade)
else:
    print("Quantidade ímpar:", quantidade)

# média de 7 temperaturas
temperaturas = []

for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / 7

print("Média da semana:", media)

#Soma apenas dos numeros pares
venda = [10, 15, 20, 9, 7, 8]

soma = 0

for v in venda:
    if v % 2 == 0:
        soma += v 

print("Soma dos pares:", soma)

#desconto na loja
valor = float(input("Digite o valor da compra: "))

if valor > 500:
    valor_final = valor * 0.8
elif valor >= 200:
    valor_final = valor * 0.9
else:
    valor_final = valor

print("Valor final:", valor_final)

#contar notas acima de 7 
notas = [float(input("digite uma nota:")) for _ in range(5)]

contador = 0

for notas in notas:
    if notas > 7:
        contador += 1 

print(f"quantidade de notas acima de 7: {contador}")

#contar vogais
frase = input("Digite uma frase: ").lower()

vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"Quantidade de vogais: {contador}")

#lista de 5 iadade de alunos em ordem crescente
idades = []

for i in range(5):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)

idades.sort()

print("Idades em ordem crescente:", idades)

while True:
    print("\n--- CALCULADORA ---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando a calculadora...")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcao == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcao == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcao == "4":
            if num2 == 0:
                print("Erro: divisão por zero!")
            else:
                resultado = num1 / num2
                print("Resultado:", resultado)

        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: digite apenas números válidos!")