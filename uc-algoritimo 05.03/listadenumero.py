numeros = [80, 20, 30, 20, 40, 90, 50]

print("Lista:", numeros)

quantidade = len(numeros)
print("Quantidade de elementos na lista:", quantidade)

vezes_20 = numeros.count(20)
print("O número 20 aparece", vezes_20, "vezes na lista")


posicao_30 = numeros.index(30)
print("A posição do número 30 é:", posicao_30)


if 100 in numeros:
    print("O número 100 está presente na lista")
else:
    print("O número 100 NÃO está presente na lista")