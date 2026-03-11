total = 0
quantidade = 0

while True:
    valor = float(input("digite o valor do depósito (0 para sair): "))

    if valor == 0:
        break

    total += valor
    quantidade += 1

print("total depositado:", total)
print("quantidade de depósitos:", quantidade)