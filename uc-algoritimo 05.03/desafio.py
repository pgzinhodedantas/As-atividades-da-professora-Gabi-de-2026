import random


numeros = [91, 34, 67, 15, 82]

print("Lista original:", numeros)

numeros.sort()
print("Lista em ordem crescente:", numeros)

numeros.sort(reverse=True)
print("Lista em ordem decrescente:", numeros)

numeros3 = [6, 7, 8, 9, 10]

random.shuffle(numeros3)
print("Lista embaralhada:", numeros3)

numeros4 = [12, 4, 25, 7, 19, 30]

print("\nLista do desafio:", numeros4)

numeros4.sort()
print("Ordem crescente:", numeros4)

numeros4.sort(reverse=True)
print("Ordem decrescente:", numeros4)

random.shuffle(numeros4)
print("Lista embaralhada:", numeros4)