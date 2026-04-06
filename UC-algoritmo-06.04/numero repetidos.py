numeros = []


for i in range(8):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

contagem = {}

for n in numeros:
    if n in contagem:
        contagem[n] += 1
    else:
        contagem[n] = 1

print("Números repetidos:")
repetidos = False

for num, qtd in contagem.items():
    if qtd > 1:
        print(f"{num} apareceu {qtd} vezes")
        repetidos = True

if not repetidos:
    print("Nenhum número ser repetido.")